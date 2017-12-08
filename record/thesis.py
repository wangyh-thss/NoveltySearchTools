# encoding=utf-8

from publication import Publication


class Thesis(Publication):
    export_format = '@{author}（导师：@{instructor}）. @{title}. @{publisher}, @{year}'

    def __init__(self, authors=None, instructor='', title='', publisher='', year=''):
        super(Thesis, self).__init__()
        if authors is None:
            authors = []
        self.authors = authors
        self.instructor = instructor
        self.title = title
        self.publisher = publisher
        self.year = year
        self.label_map = {
            '@{author}': self.concat_authors(self.authors),
            '@{instructor}': self.instructor,
            '@{title}': self.title,
            '@{publisher}': self.publisher,
            '@{year}': self.year,
        }
