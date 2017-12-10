# -*- coding:utf-8 -*-

from pybtex.database import parse_file, parse_string
from article_parser import ArticleParser
from record.publication import Publication


class BibParser(ArticleParser):

    def __init__(self):
        super(BibParser, self).__init__()

    def parse_string(self, content):
        try:
            bib_data = parse_string(content, bib_format='bibtex')
            return self.convert(bib_data)
        except:
            return None

    def parse_file(self, filename):
        bib_data = parse_file(filename)
        return self.convert(bib_data)

    @staticmethod
    def convert(bib_data):
        return Publication()
