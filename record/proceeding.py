# -*- coding:utf-8 -*-

from publication import Publication


class Proceeding(Publication):
    format_conference = '@{author}. @{title}[C]: @{conference name}, ' \
                        '@{conference address}, @{date}. @{institute}'
    format_proceeding = '@{author}. @{title}[C]: @{proceeding}, ' \
                        '@{publish address}:@{publisher}, @{year}:@{pages}'
    export_format = format_proceeding

    def __init__(self, ptype='proceeding', authors=None, title='', conference_name='', conference_address='', pages='',
                 date='', institute='', proceeding='', publish_address='', publisher='', year=''):
        super(Proceeding, self).__init__()
        if authors is None:
            authors = []
        self.type = ptype    # or proceeding
        self.format_conference = '@{author}. @{title}[C]: @{conference name}, ' \
                                 '@{conference address}, @{date}. @{institute}'
        self.format_proceeding = '@{author}. @{title}[C]: @{proceeding}, ' \
                                 '@{publish address}:@{publisher}, @{year}:@{pages}'
        if self.type == 'conference':
            self.export_format = self.format_conference
        else:
            self.export_format = self.format_proceeding

        self.authors = authors
        self.title = title
        self.conference_name = conference_name
        self.conference_address = conference_address
        self.date = date
        self.institute = institute
        self.proceeding = proceeding
        self.publish_address = publish_address
        self.year = year
        self.publisher = publisher
        self.pages = pages
