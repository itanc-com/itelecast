import logging

from app.core.pydantic.settings import EnvironmentType


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    pink = "\x1b[95m"
    cyan = "\x1b[36m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"  # ANSI code to reset color

    format = "\n%(levelname)s : %(message)s (%(filename)s:%(lineno)d)\n"

    FORMATS = {
        logging.DEBUG: pink + format + reset,
        logging.INFO: cyan + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def configure_logger(environment: EnvironmentType) -> None:
    logger = logging.getLogger()

    if environment in (EnvironmentType.PRODUCTION, EnvironmentType.STAGING):
        logger.setLevel(logging.INFO)
    elif environment == EnvironmentType.DEVELOPMENT:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    stream_handler = logging.StreamHandler()
    custom_formatter = CustomFormatter()
    stream_handler.setFormatter(custom_formatter)

    logger.addHandler(stream_handler)
