# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging


# TODO: Use basicConfig to configure logging

logging.basicConfig(
    level=logging.DEBUG, filename="Start/Ch_4/output.log", filemode="w"
)  # This will configure to show all levels of logging messages

# TODO: Try out each of the log levels

logging.debug("This is a debug level message.")
logging.info("This is an info level message.")
logging.warning("This is a warning level message.")
logging.error("This is an error level message.")
logging.critical("This is a critical level message.")

# TODO: Output formatted strings to the log
x = "hi bubs"
y = 10

logging.info(f"Here's a string: '{x}' and integer: {y}")
