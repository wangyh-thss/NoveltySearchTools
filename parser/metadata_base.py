# -*- coding:utf-8 -*-

import json
from record import Achievement, Journal, Patent, Proceeding, Thesis
from common.constants import Constants


class MetadataBase(object):
    separator = ','
    type_label_dict = {
        Constants.LABEL_ARTICLE_TYPE: {'{Reference Type}:', 'PT'},
        Constants.LABEL_AUTHOR: {'{Author}:', 'AU'},
        Constants.LABEL_TITLE: {'{Title}:'},
        Constants.LABEL_KEYWORD: {'{Keywords}:'},
        Constants.LABEL_JOURNAL: {'{Journal}:'},
        Constants.LABEL_YEAR: {'{Year}:'},
        Constants.LABEL_DATE: {'{Date}:'},
        Constants.LABEL_VOLUME: {'{Volume}:'},
        Constants.LABEL_PAGES: {'{Pages}:'},
        Constants.LABEL_ISSUE: {'{Issue}:'},
        Constants.LABEL_INSTITUTE: {'{Author Address}:'},
        Constants.LABEL_PUBLISH_DATE: {'{Reviewed Item}:'},
        Constants.LABEL_ABSTRACT: {'{Abstract}:'},
        Constants.LABEL_PROCEEDING: {'{Tertiary Title}:'},
        Constants.LABEL_PUBLISH_ADDRESS: {'{Place Published}:'},
        Constants.LABEL_PUBLISHER: {'{Subsidiary Author}:', '{Publisher}:'},
        Constants.LABEL_CONFERENCE_NAME: {'{Secondary Title}:'},
        Constants.LABEL_CONFERENCE_ADDRESS: {},
        Constants.LABEL_INSTRUCTOR: {'{Tertiary Author}:'},
    }

    type_desc_dict = {
        Constants.LABEL_ARTICLE_TYPE: '文献类型',
        Constants.LABEL_AUTHOR: '作者',
        Constants.LABEL_TITLE: '题名',
        Constants.LABEL_KEYWORD: '关键词',
        Constants.LABEL_JOURNAL: '刊名',
        Constants.LABEL_YEAR: '年份',
        Constants.LABEL_DATE: '日期',
        Constants.LABEL_VOLUME: '卷',
        Constants.LABEL_PAGES: '页码',
        Constants.LABEL_ISSUE: '期',
        Constants.LABEL_INSTITUTE: '作者机构/地址',
        Constants.LABEL_PUBLISH_DATE: '出版日期/公开日期',
        Constants.LABEL_ABSTRACT: '摘要',
        Constants.LABEL_PROCEEDING: '论文集',
        Constants.LABEL_PUBLISH_ADDRESS: '出版地',
        Constants.LABEL_PUBLISHER: '出版社/专利权人',
        Constants.LABEL_CONFERENCE_NAME: '会议名称',
        Constants.LABEL_CONFERENCE_ADDRESS: '会议地址',
        Constants.LABEL_INSTRUCTOR: '导师',
    }

    article_class_label_dict = {
        Constants.PUBLICATION_ACHIEVEMENT: {'Generic'},
        Constants.PUBLICATION_JOURNAL: {'Journal Article', 'Article'},
        Constants.PUBLICATION_PATENT: {'Patent', 'P'},
        Constants.PUBLICATION_PROCEEDING: {'Conference Proceedings'},
        Constants.PUBLICATION_THESIS: {'Thesis'},
    }

    article_class_dict = {
        Constants.PUBLICATION_ACHIEVEMENT: Achievement,
        Constants.PUBLICATION_JOURNAL: Journal,
        Constants.PUBLICATION_PATENT: Patent,
        Constants.PUBLICATION_PROCEEDING: Proceeding,
        Constants.PUBLICATION_THESIS: Thesis,
    }

    def __init__(self):
        pass

    @classmethod
    def set_type_labels(cls, label_type, message):
        labels = message.split(cls.separator)
        cls.type_label_dict[label_type] = set(labels)

    @classmethod
    def get_types(cls):
        return cls.type_label_dict.keys()

    @classmethod
    def get_labels(cls, label_name):
        return cls.type_label_dict.get(label_name, set())

    @classmethod
    def get_article_type(cls, value):
        for article_type, value_set in cls.article_class_label_dict.items():
            if value in value_set:
                return article_type
        return None

    @classmethod
    def create_empty_record(cls, article_type):
        if article_type not in cls.article_class_dict:
            return None
        return cls.article_class_dict[article_type]()

    @classmethod
    def create_record(cls, data_dict):
        record = cls.create_empty_record(data_dict.get(Constants.LABEL_ARTICLE_TYPE))
        if record is None:
            return None
        for attr, value in data_dict.items():
            if attr == Constants.LABEL_AUTHOR:
                record.set_authors(value)
            elif attr == Constants.LABEL_KEYWORD:
                record.set_keywords(value)
            else:
                record.set_attr(attr, value)
        return record

    @classmethod
    def save(cls, filename):
        save_obj = dict()
        save_items = ['type_label_dict', 'article_class_label_dict']
        for item in save_items:
            item_dict = getattr(cls, item)
            temp_obj = dict()
            for key, value in item_dict.items():
                temp_obj[key] = list(value)
            save_obj[item] = temp_obj
        with open(filename, 'w') as f:
            json.dump(save_obj, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            load_obj = json.load(f)
        for item, item_dict in load_obj.items():
            for key, value in item_dict.items():
                item_dict[key] = set(value)
            setattr(cls, item, item_dict)

    @classmethod
    def get_label_string(cls, label_name):
        labels = cls.type_label_dict.get(label_name)
        if labels is None:
            return ''
        return ';'.join(labels)

    @classmethod
    def set_label(cls, label_name, label_string):
        if label_string == '':
            return
        labels = label_string.split(';')
        cls.type_label_dict[label_name] = set(labels)

    @classmethod
    def get_class_string(cls, class_name):
        tags = cls.article_class_label_dict.get(class_name)
        if tags is None:
            return ''
        return ';'.join(tags)

    @classmethod
    def set_class_tag(cls, class_name, tag_string):
        if tag_string == '':
            return
        labels = tag_string.split(';')
        cls.article_class_label_dict[class_name] = set(labels)
