import logging

__author__ = 'olli'

import datetime
import time
import requests
import requests.exceptions
import web_page

_logger = logging.getLogger('poller')
_logger.setLevel(logging.INFO)


def update(webpage):
    """
    Update the status of given WebPage
    :type webpage: web_page.WebPage
    :param webpage: WebPage object
    :return:
    """
    webpage.last_checked = datetime.datetime.now()
    try:
        start_at = time.time()
        request = _read(webpage.url)
        end_at = time.time()
        print "HERE"
        _set_stats(webpage, request, int(round((end_at - start_at) * 1000)))
    except requests.exceptions.RequestException, e:
        # Catch any exception from 'requests' library
        # TODO: separate handling of different connection or HTTP parsing errors
        _set_fail_stats(webpage, e)
        print "Exception on  " + webpage.url + " EXCEPTION: " + str(e) + " TYPE: " + str(type(e))

    _validate_results(webpage)


def _read(url):
    return requests.get(url, )


def _set_stats(webpage, request, response_time):
    webpage.connection_state = "OK"
    webpage.response_time = response_time
    webpage.actual_status_code = request.status_code
    webpage.actual_content_type = request.headers['Content-Type']


def _set_fail_stats(webpage, error):
    webpage.connection_state = str(type(error))
    webpage.response_time = None
    webpage.actual_status_code = None
    webpage.actual_content_type = None


def _validate_results(webpage):
    if webpage.connection_state is not "OK" or webpage.actual_status_code is not webpage.expected_status_code \
            or not webpage.actual_content_type.startswith(webpage.expected_content_type):
        test_status = "FAIL"
    else:
        test_status = "OK"

    # Finally log the poll event results to file
    _logger.info("{0} {1}".format(test_status, str(webpage)))
