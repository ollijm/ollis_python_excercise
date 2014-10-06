__author__ = 'olli'


class WebPage:
    """
    WebPage represents the state of a web resource that we monitor
    """
    def __init__(self, url, expected_status_code, expected_content_type):
        self._url = url
        self._expected_status_code = expected_status_code
        self._actual_status_code = None
        self._expected_content_type = expected_content_type
        self._actual_content_type = None
        self._response_time = None
        self._last_checked = None

    def __str__(self):
        s = "url='{0}' " \
            "status_code='{1}' " \
            "expected_status_code='{2}' " \
            "content_type='{3}' " \
            "expected_content_type='{4}' " \
            "response_time='{5}' " \
            "last_checked='{6}'".format(self.url, self.actual_status_code, self.expected_status_code,
                                        self.actual_content_type, self.expected_content_type, self.response_time,
                                        self.last_checked)
        return s

    @property
    def url(self):
        return self._url

    @property
    def expected_status_code(self):
        return self._expected_status_code

    @property
    def actual_status_code(self):
        return self._actual_status_code

    @property
    def expected_content_type(self):
        return self._expected_content_type

    @property
    def actual_content_type(self):
        return self._actual_content_type

    @property
    def response_time(self):
        """In milliseconds"""
        return self._response_time

    @property
    def last_checked(self):
        return self._last_checked

    @actual_status_code.setter
    def actual_status_code(self, value):
        self._actual_status_code = value

    @actual_content_type.setter
    def actual_content_type(self, value):
        self._actual_content_type = value

    @response_time.setter
    def response_time(self, value):
        self._response_time = value

    @last_checked.setter
    def last_checked(self, value):
        self._last_checked = value