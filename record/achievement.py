# encoding=utf-8

from publication import Publication


class Achievement(Publication):
    export_format = '@{author}. @{title}[Z]. @{year}. @{institute}'

    def __init__(self, authors=None, title='', year='', institute=''):
        super(Achievement, self).__init__()
        if authors is None:
            authors = []
        self.authors = authors
        self.title = title
        self.year = year
        self.institute = institute
        self.label_map = {
            '@{author}': self.concat_authors(self.authors),
            '@{title}': self.title,
            '@{year}': self.year,
            '@{institute}': self.institute,
        }
