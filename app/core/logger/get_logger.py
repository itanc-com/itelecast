import logging


def get_logger() -> logging.Logger:
    logger = logging.getLogger("itelecast")  # Creates a named logger
    return logger
