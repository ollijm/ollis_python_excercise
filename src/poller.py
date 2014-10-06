import logging

__author__ = 'olli'

import datetime
import time
import requests
import requests.exceptions
import web_page
import validator

_logger = logging.getLogger('poller')
_logger.setLevel(logging.INFO)


def update(page):
    """
    Update the status of given WebPage
    :type page: web_page.WebPage
    :param page: WebPage object
    :return:
    """
    page.last_checked = datetime.datetime.now()
    try:
        start_at = time.time()
        request = _read(page.url)
        end_at = time.time()
        _set_stats(page, request, int(round((end_at - start_at) * 1000)))
    except requests.exceptions.RequestException, e:
        # Catch any exception from 'requests' library
        # TODO: separate handling of different connection or HTTP parsing errors
        _set_fail_stats(page, e)

    _validate_results(page)


def _read(url):
    return requests.get(url, )


def _set_stats(page, request, response_time):
    page.connection_state = "OK"
    page.response_time = response_time
    page.actual_status_code = request.status_code
    page.actual_content_type = request.headers['Content-Type']


def _set_fail_stats(page, error):
    print "Setting error on page " + page.url
    page.connection_state = error.__class__.__name__
    page.response_time = None
    page.actual_status_code = None
    page.actual_content_type = None
    print "FINALLY: " + str(page)


def _validate_results(page):
    if validator.validate_web_page(page):
        test_status = "OK"
    else:
        test_status = "FAIL"

    # Finally log the poll event results to file
    _logger.info("{0} {1}".format(test_status, str(page)))
