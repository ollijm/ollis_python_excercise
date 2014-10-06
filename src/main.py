__author__ = 'olli'

import config
import validator
import sys
import scheduler

print str(sys.argv)


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

conf = config.Config("/dummy/path")
conf.initialize()
scheduler.start(interval, conf)