# encoding=utf-8

from article_parser import ArticleParser
from metadata_base import MetadataBase
from common.constants import Constants


def parse_label(line):
    for label_type in MetadataBase.get_types():
        for label in MetadataBase.get_labels(label_type):
            try:
                index = line.index(label)
            except ValueError:
                continue
            value = line[index + len(label):]
            return label_type, label, value.strip()
    return None, None, None


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
        label_type, label, value = parse_label(line)
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


def split_content(content):
    result = list()
    lines = content.splitlines()
    record_data = list()
    for line in lines:
        if line == '':
            result.append(record_data)
            record_data = list()
        record_data.append(line)
    return result


class MultiLinesParser(ArticleParser):

    def __init__(self):
        super(MultiLinesParser, self).__init__()

    def parse_string(self, content):
        result = list()
        records_data = split_content(content)
        for record_data in records_data:
            record = parse_record(record_data)
            if record is None:
                continue
            result.append(record)
        return result


if __name__ == '__main__':
    parser = MultiLinesParser()
    r = parser.parse_file('../../doc/格式二-2017年9月13日 14_34_56@WanFangdata.Net')
    for a in r:
        print a.export()
