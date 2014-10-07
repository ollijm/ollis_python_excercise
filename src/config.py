import urls
import web_page


class Config:
    """
    Reads web page and their requirement list from urls.py and exposes access to the WebPage object list
    """

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
        """
        Read configuration file into WebPage objects
        :return:
        """
        for url_dict in urls.urls:
            page = web_page.WebPage(url_dict['url'], url_dict['expected_status_code'],
                                    url_dict['expected_content_type'])
            self.web_pages.append(page)