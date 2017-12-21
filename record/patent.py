# -*- coding:utf-8 -*-

from publication import Publication


class Patent(Publication):
    export_format = '@{authors}. @{title}:@{issue}[P]. @{publish date}. @{publisher}\r\n' \
                    '【摘要】@{abstract}\r\n【主题词】@{keywords}\r\n【多余的其他信息】@{others}'

    def __init__(self, authors=None, title='', issue='', publish_date='', publisher='', abstract='', keywords='', others=''):
        super(Patent, self).__init__()
        if authors is None:
            authors = []
        if keywords is None:
            keywords = []
        self.authors = authors
        self.title = title
        self.issue = issue
        self.publish_date = publish_date
        self.publisher = publisher
        self.others = others
        self.abstract = abstract
        self.keywords = keywords
