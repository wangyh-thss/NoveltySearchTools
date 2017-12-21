# -*- coding:utf-8 -*-

from publication import Publication


class Journal(Publication):
    export_format = '@{authors}. @{title}[J]. @{journal}, @{year},@{volume}(@{issue}):@{pages}. @{institute}'

    def __init__(self, title='', journal='', authors=None, year='', pages='', volume='', institute='', issue=''):
        super(Journal, self).__init__()
        if authors is None:
            authors = []
        self.title = title
        self.journal = journal
        self.authors = authors
        self.year = year
        self.pages = pages
        self.volume = volume
        self.institute = institute
        self.issue = issue
