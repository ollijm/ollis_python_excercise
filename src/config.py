__author__ = 'olli'


import unittest
import web_page


class Config:

    def __init__(self, config_file):
        """
        :param config_file:
        :return:
        """
        self._config_file = config_file
        self.url_targets = []

    @property
    def config_file(self):
        return self._config_file

    @property
    def url_targets(self):
        return self._url_targets

    def initialize(self):
        # TODO: Read from file
        u1 = web_page.WebPage("http://www.kaleva.fi/", 200, "text/html")
        u2 = web_page.WebPage("http://www.iltasanomat.fi/rss/uutiset.xml", 200, "text/xml")
        u3 = web_page.WebPage("http://www.google.fi/", 200, "text/html")

        self.url_targets.append(u1)
        self.url_targets.append(u2)
        self.url_targets.append(u3)


class ConfigTest(unittest.TestCase):
    def test_instantiate(self):
        config = Config("/path/to/file")
        config.initialize()
        for url_target in config.url_targets:
            print str(url_target)

if __name__ == '__main__':
    unittest.main()