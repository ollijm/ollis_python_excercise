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
        self._web_pages = []

    @property
    def config_file(self):
        return self._config_file

    @property
    def web_pages(self):
        return self._web_pages

    def initialize(self):
        # TODO: Read from file
        u1 = web_page.WebPage("http://www.kaleva.fi/", 200, "text/html")
        u2 = web_page.WebPage("http://www.iltasanomat.fi/rss/uutiset.xml", 200, "text/xml")
        u3 = web_page.WebPage("http://www.google.fi/", 200, "text/html")
        u4 = web_page.WebPage("http://www.reallynotexistingdomainxyz.fi/", 200, "text/html")
        u5 = web_page.WebPage("http://www.google.fi/not-existing-file.html", 200, "text/html")
        u6 = web_page.WebPage("htp:///this.might.not.work.html", 200, "text/html")

        self.web_pages.append(u1)
        self.web_pages.append(u2)
        self.web_pages.append(u3)
        self.web_pages.append(u4)
        self.web_pages.append(u5)
        self.web_pages.append(u6)


class ConfigTest(unittest.TestCase):
    """
    Unit Test so to speak...
    """
    def test_instantiate(self):
        config = Config("/path/to/file")
        config.initialize()
        for url_target in config.web_pages:
            print str(url_target)

if __name__ == '__main__':
    unittest.main()