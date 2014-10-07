"""
Main executable module of Olli's Web Monitor
Usage: python src/main.py 30
where 30 is the time interval during which all web pages are checked once
"""

import sys
import logging
import thread

import config
import validator
import scheduler
import web_server


logging.basicConfig(format="%(asctime)s %(message)s", filename="request.log")

# Set default interval or validate value from command line args
if len(sys.argv) == 1:
    interval = 10
else:
    if validator.is_stringinteger(sys.argv[1]):
        interval = int(sys.argv[1])
    else:
        print "First parameter must be value for poll interval in seconds."
        print "Please enter integer as first parameter."
        print "Example: python main.py 60"
        sys.exit(1)

if interval < 10:
    print "Setting poll interval to the minimum of 10 seconds."
    interval = 10

# Initialize config object to be passed around
# It contains access to our WebPage objects
conf = config.Config()
conf.initialize()

# Start the web server
web_server.conf = conf
thread.start_new_thread(web_server.start, ())

# Start main polling loop
scheduler.start(interval, conf)