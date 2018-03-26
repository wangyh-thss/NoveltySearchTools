# -*- coding:utf-8 -*-

from article_parser import ArticleParser
from common.constants import Constants
from common.publish_helper import build_output
from metadata_base import MetadataBase


def parse_label(line):
    labels = list()
    for label_type in MetadataBase.get_types():
        for label in MetadataBase.get_labels(label_type):
            try:
                index = line.index(label)
            except ValueError:
                continue
            value = line[index + len(label):].strip()
            labels.append((label_type, label, value))
    if not labels:
        labels.append((None, None, None))
    return labels


def insert_value(data_dict, label_type, value):
    if label_type not in data_dict:
        data_dict[label_type] = []
    data_dict[label_type].append(value)


def update_data_dict(data_dict, label_type, value):
    if label_type == Constants.LABEL_ARTICLE_TYPE:
        article_type = MetadataBase.get_article_type(value)
        data_dict[label_type] = article_type
    elif label_type in {Constants.LABEL_AUTHOR, Constants.LABEL_KEYWORD, Constants.LABEL_OTHERS}:
        insert_value(data_dict, label_type, value)
    else:
        data_dict[label_type] = value


def parse_record(record_data):
    data_dict = dict()
    last_label_type = None
    for line in record_data:
        if not record_data:
            continue
        labels = parse_label(line)
        for label_type, label, value in labels:
            if label_type is None:
                value = line.strip()
                if value != line:
                    label_type = last_label_type
                else:
                    label_type = Constants.LABEL_OTHERS
            update_data_dict(data_dict, label_type, value)
            last_label_type = label_type
    if Constants.LABEL_OTHERS in data_dict:
        data_dict[Constants.LABEL_OTHERS] = '\r\n'.join(data_dict[Constants.LABEL_OTHERS])
    record = MetadataBase.create_record(data_dict)
    return record


class MultiLinesParser(ArticleParser):

    def __init__(self):
        super(MultiLinesParser, self).__init__()

    def parse_string(self, content):
        result = list()
        records_data = self.split_content(content)
        for record_data in records_data:
            record = parse_record(record_data)
            if record is None:
                continue
            result.append(record)
        return result

    @classmethod
    def split_content(cls, content):
        result = list()
        lines = content.splitlines()
        record_data = list()
        recorded = False
        for line in lines:
            if cls.is_split_line(line):
                if recorded:
                    result.append(record_data)
                    record_data = [line]
                else:
                    record_data.append(line)
                    recorded = True
            elif recorded:
                record_data.append(line)
        result.append(record_data)
        return result

    @classmethod
    def is_split_line(cls, line):
        for begin_label in MetadataBase.begin_labels:
            if line.startswith(begin_label):
                return True
        return False


if __name__ == '__main__':
    parser = MultiLinesParser()
    r = parser.parse_file('../../doc/格式二-2017年9月13日 14_34_56@WanFangdata.Net')
    print build_output(r)
