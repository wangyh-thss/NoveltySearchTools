# -*- coding:utf-8 -*-

from publication import Publication


class Thesis(Publication):
    export_format = '@{author}（导师：@{instructor}）. @{title}[D]. @{publisher}, @{year}'

    def __init__(self, authors=None, instructor='', title='', publisher='', year=''):
        super(Thesis, self).__init__()
        if authors is None:
            authors = []
        self.authors = authors
        self.instructor = instructor
        self.title = title
        self.publisher = publisher
        self.year = year
