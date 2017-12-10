# -*- coding:utf-8 -*-

from constants import Constants
from record import Achievement, Journal, Patent, Proceeding, Thesis

class_type_dict = {
    Achievement: Constants.PUBLICATION_ACHIEVEMENT,
    Journal: Constants.PUBLICATION_JOURNAL,
    Patent: Constants.PUBLICATION_PATENT,
    Proceeding: Constants.PUBLICATION_PROCEEDING,
    Thesis: Constants.PUBLICATION_THESIS,
}


def remove_duplicate(category_dict):
    return category_dict


def build_output_str(category_dict, type_order):
    content = ''
    publish_count = 0
    for publish_type in type_order:
        if publish_type not in category_dict:
            continue
        publish_list = category_dict[publish_type]
        content += u'共有%s篇%s:\r\n' % (len(publish_list), Constants.ARTICLE_CLASS_DESC.get(publish_type))
        for publish in publish_list:
            publish_count += 1
            content += u'%s. %s\r\n\r\n' % (publish_count, publish.export())
    return content


def build_output(publish_list):
    publish_type_list = [
        Constants.PUBLICATION_JOURNAL,
        Constants.PUBLICATION_THESIS,
        Constants.PUBLICATION_PROCEEDING,
        Constants.PUBLICATION_ACHIEVEMENT,
        Constants.PUBLICATION_PATENT
    ]
    category_dict = dict()
    for publish in publish_list:
        category = class_type_dict.get(type(publish))
        if category is None:
            continue
        category_dict.setdefault(category, []).append(publish)
    category_dict = remove_duplicate(category_dict)
    return build_output_str(category_dict, publish_type_list)

