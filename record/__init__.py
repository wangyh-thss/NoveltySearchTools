# -*- coding:utf-8 -*-

import json
import sys
from common.constants import Constants
from achievement import Achievement
from journal import Journal
from patent import Patent
from proceeding import Proceeding
from publication import Publication
from thesis import Thesis

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")

default_format_file = 'format'

article_class_dict = {
    Constants.PUBLICATION_ACHIEVEMENT: Achievement,
    Constants.PUBLICATION_JOURNAL: Journal,
    Constants.PUBLICATION_PATENT: Patent,
    Constants.PUBLICATION_PROCEEDING: Proceeding,
    Constants.PUBLICATION_THESIS: Thesis,
}


def load_format(filename):
    with open(filename, 'r') as f:
        format_dict = json.load(f)
    for article_class, article_type in article_class_dict.items():
        output_format = format_dict.get(article_class)
        if output_format is not None and output_format != '':
            article_type.set_export_format(output_format)


def save_format(filename):
    format_dict = dict()
    for article_class, article_type in article_class_dict.items():
        format_dict[article_class] = article_type.export_format
    with open(filename, 'w') as f:
        json.dump(format_dict, f)


try:
    load_format(default_format_file)
except IOError:
    pass
