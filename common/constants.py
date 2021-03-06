# -*- coding:utf-8 -*-


class PublishSimilarity:

    def __init__(self):
        pass

    SAME = 0
    SIMILAR = 1
    DIFFERENT = 2


class Constants:

    def __init__(self):
        pass

    LABEL_ARTICLE_TYPE = 'article_type'
    LABEL_AUTHOR = 'authors'
    LABEL_TITLE = 'title'
    LABEL_YEAR = 'year'
    LABEL_DATE = 'date'
    LABEL_OTHERS = 'others'
    LABEL_KEYWORD = 'keywords'
    LABEL_JOURNAL = 'journal'
    LABEL_PAGES = 'pages'
    LABEL_VOLUME = 'volume'
    LABEL_ABSTRACT = 'abstract'
    LABEL_ISSUE = 'issue'
    LABEL_INSTITUTE = 'institute'
    LABEL_PROCEEDING = 'proceeding'
    LABEL_PUBLISH_DATE = 'publish_date'
    LABEL_PUBLISH_ADDRESS = 'publish_address'
    LABEL_PUBLISHER = 'publisher'
    LABEL_CONFERENCE_NAME = 'conference_name'
    LABEL_CONFERENCE_ADDRESS = 'conference_address'
    LABEL_INSTRUCTOR = 'instructor'

    PUBLICATION_ACHIEVEMENT = 'achievement'
    PUBLICATION_JOURNAL = 'journal'
    PUBLICATION_PATENT = 'patent'
    PUBLICATION_PROCEEDING = 'proceeding'
    PUBLICATION_THESIS = 'thesis'

    ARTICLE_CLASS_DESC = {
        PUBLICATION_ACHIEVEMENT: '科技成果',
        PUBLICATION_JOURNAL: '期刊',
        PUBLICATION_PATENT: '专利',
        PUBLICATION_PROCEEDING: '会议论文',
        PUBLICATION_THESIS: '学位论文',
    }

    @staticmethod
    def format_label(label_name):
        return ('@{%s}' % label_name).replace(' ', '_')

