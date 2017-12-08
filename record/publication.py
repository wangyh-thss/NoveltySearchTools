# encoding=utf-8

import re
from common.constants import Constants


class Publication(object):
    export_format = ''

    def __init__(self):
        self.label_map = {}

    def export(self):
        export_str = self.export_format
        labels = re.findall(r'@{.*?}', export_str)
        for label in labels:
            value = self.label_map.get(label)
            if value is None:
                try:
                    value = getattr(self, label.replace(' ', '_'))
                except AttributeError:
                    value = label
            if type(value) not in [str, unicode]:
                value = str(value)
            export_str = export_str.replace(label, value)
        return export_str

    def set_authors(self, authors):
        setattr(self, Constants.LABEL_AUTHOR, authors)
        self.label_map['@{author}'] = self.concat_authors(authors)

    def set_keywords(self, keywords):
        setattr(self, Constants.LABEL_KEYWORD, keywords)
        self.label_map['@{%s}' % Constants.LABEL_KEYWORD] = self.concat_keywords(keywords)

    def set_attr(self, attr, value):
        setattr(self, attr, value)
        label_name = ('@{%s}' % attr).replace('_', ' ')
        self.label_map[label_name] = value

    @classmethod
    def set_export_format(cls, format_str):
        cls.export_format = format_str

    @staticmethod
    def concat_authors(authors):
        return ', '.join(authors)

    @staticmethod
    def concat_keywords(keywords):
        return ', '.join(keywords)