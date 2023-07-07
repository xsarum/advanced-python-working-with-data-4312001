# Demonstrate how to customize logging output

import logging


def another_function():
    logging.debug("This is a debug level log message.", extra=EXT_DATA)


# TODO: add another function to log from
FRMT_STR = "User %(user)s: %(asctime)s: %(levelname)s: %(funcName)s: Line: %(lineno)d %(message)s"
DATE_STR = " %m/%d/%Y %I-%M-%S %p"
EXT_DATA = {"user": "annabellesmith@kubrickgroup.com"}
# set the output file and debug level, and
# TODO: use a custom formatting specification
logging.basicConfig(
    filename="Start/Ch_4/custom_output.log",
    level=logging.DEBUG,
    format=FRMT_STR,
    datefmt=DATE_STR,
)

logging.info("This is an info-level log message", extra=EXT_DATA)
logging.warning("This is a warning-level message", extra=EXT_DATA)

another_function()
