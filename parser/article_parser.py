# encoding=utf-8


class ArticleParser(object):

    def __init__(self):
        pass

    def parse_string(self, content):
        pass

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            content = f.read()
        return self.parse_string(content)
