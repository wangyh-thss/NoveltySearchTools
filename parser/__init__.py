# -*- coding:utf-8 -*-

import sys
from bib_parser import BibParser
from multi_lines_parser import MultiLinesParser
from metadata_base import MetadataBase

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")

default_metadata_filename = 'config'
try:
    MetadataBase.load(default_metadata_filename)
except IOError:
    pass

