__author__ = 'olli'

import poller
import time


def start(interval, conf):
    """
    The main loop of the program fetches the list of URLs and sleeps until interval is passed
    :param interval: Interval in seconds
    :type interval: int
    :param conf: Config object
    :type conf: config.Config
    :return:
    """
    print "Starting scheduler..."

    cont = True
    while cont:
        loop_started = time.time()
        for web_page in conf.web_pages:
            print web_page.url
            poller.update(web_page)
        print "Sleeping {0} seconds.".format(interval)
        _sleep_until_interval(loop_started, interval)


def _sleep_until_interval(loop_started, interval):
    loop_length = time.time() - loop_started
    if loop_length < interval:
        time.sleep(interval - loop_length)
    pass