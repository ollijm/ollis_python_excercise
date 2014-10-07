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
    # TODO: configure timeouts etc
    return requests.get(url, )


def _set_stats(page, request, response_time):
    page.read_state = "OK"
    page.response_time = response_time
    page.actual_status_code = request.status_code
    if request.headers['Content-Type']:
        page.actual_content_type = request.headers['Content-Type']
    else:
        page.actual_content_type = None


def _set_fail_stats(page, error):
    page.read_state = error.__class__.__name__
    page.response_time = None
    page.actual_status_code = None
    page.actual_content_type = None


def _validate_results(page):
    test_status = validator.web_page_status_as_string(page)

    # Finally log the poll event results to file
    _logger.info("{0} {1}".format(test_status, str(page)))
