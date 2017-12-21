# -*- coding:utf-8 -*-

from publication import Publication


class Proceeding(Publication):
    format_conference = '@{authors}. @{title}[C]: @{conference name}, ' \
                        '@{conference address}, @{date}. @{institute}'
    format_proceeding = '@{authors}. @{title}[C]: @{proceeding}, ' \
                        '@{publish address}:@{publisher}, @{year}:@{pages}'
    export_format = format_conference

    def __init__(self, ptype='conference', authors=None, title='', conference_name='', conference_address='', pages='',
                 date='', institute='', proceeding='', publish_address='', publisher='', year=''):
        super(Proceeding, self).__init__()
        if authors is None:
            authors = []
        self.ptype = ptype    # or proceeding
        if self.ptype == 'conference':
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
