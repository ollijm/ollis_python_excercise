__author__ = 'olli'

import poller
import time

def start(interval, conf):
    """
    :param interval: Interval in seconds
    :type interval: int
    :param conf: Config object
    :type conf: config.Config
    :return:
    """
    print "Starting scheduler..."
    i = 0
    while i < 1:
        i += 1
        for web_page in conf.web_pages:
            print web_page.url
            poller.update(web_page)
        print "Sleeping {0} seconds.".format(interval)
        time.sleep(interval)