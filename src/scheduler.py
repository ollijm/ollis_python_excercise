__author__ = 'olli'

import poller
import time


def start(interval, conf):
    """
    The main loop of the program fetches the list of URLs and sleeps until interval is passed.
    If the interval is exceeded during the URL fetching, the loop continues without sleep.
    :param interval: Interval in seconds
    :type interval: int
    :param conf: Config object
    :type conf: config.Config
    :return:
    """
    while True:
        loop_started = time.time()
        for web_page in conf.web_pages:
            poller.update(web_page)
        _sleep_until_interval(loop_started, interval)


def _sleep_until_interval(loop_started, interval):
    """
    If last loop started less than interval ago, sleep until interval full
    :param loop_started:
    :param interval:
    :return:
    """
    loop_length = time.time() - loop_started
    if loop_length < interval:
        time.sleep(interval - loop_length)
    pass