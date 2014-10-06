__author__ = 'olli'

import datetime
import time
import requests
import web_page


def update(webpage):
    """
    Update the status of given WebPage
    :type webpage: web_page.WebPage
    :param webpage: WebPage object
    :return:
    """

    start_at = time.time()
    r = requests.get(webpage.url)
    end_at = time.time()
    webpage.response_time = int(round((end_at - start_at) * 1000))
    webpage.last_checked = datetime.datetime.now()
    webpage.actual_status_code = r.status_code
    webpage.actual_content_type = r.headers['Content-Type']