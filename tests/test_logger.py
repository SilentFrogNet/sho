import pytest

from sho.utils.logger import Logger, LogTypes

# --- [DATA] --- #
logger_types = [
    None,
    LogTypes.NO_LOG,
    LogTypes.TO_SCREEN,
    LogTypes.TO_COLORED_SCREEN,
    LogTypes.TO_FILE
]
logger_can_log = {
    LogTypes.NO_LOG: False,
    LogTypes.TO_SCREEN: True,
    LogTypes.TO_COLORED_SCREEN: True,
    LogTypes.TO_FILE: True
}
# --- [/DATA] --- #


# --- [FIXTURES] --- #
@pytest.fixture(params=logger_types)
def logger(request):
    """ Creates Logger fixture to use in other tests"""
    return Logger(type=request.param)


# --- [/FIXTURES] --- #


# --- [SUPPORT FUNCTIONS] --- #
# --- [/SUPPORT FUNCTIONS] --- #


# --- [TESTS] --- #
def test_create_logger(logger: Logger) -> None:
    """ Tests the creation of a Logger instance """
    assert isinstance(logger, Logger), "No valid instance of Logger"


# def test_create_logger() -> None:
#     """ Tests the creation of a Logger instance """
#     logger = Logger()
#     assert isinstance(logger, Logger), "No valid instance of Logger"
#
#
# def test_create_logger_no_log() -> None:
#     """ Tests the creation of a Logger instance """
#     logger = Logger(type=LogTypes.NO_LOG)
#     assert isinstance(logger, Logger), "No valid instance of Logger"
#
#
# def test_create_logger_to_screen() -> None:
#     """ Tests the creation of a Logger instance """
#     logger = Logger(type=LogTypes.TO_SCREEN)
#     assert isinstance(logger, Logger), "No valid instance of Logger"
#
#
# def test_create_logger_to_colored_screen() -> None:
#     """ Tests the creation of a Logger instance """
#     logger = Logger(type=LogTypes.TO_COLORED_SCREEN)
#     assert isinstance(logger, Logger), "No valid instance of Logger"
#
#
# def test_create_logger_to_file() -> None:
#     """ Tests the creation of a Logger instance """
#     logger = Logger(type=LogTypes.TO_FILE)
#     assert isinstance(logger, Logger), "No valid instance of Logger"


def test_log_can_log(logger: Logger) -> None:
    """ Tests if the logger can log """
    can_log = logger.can_log()
    assert can_log == logger_can_log.get(logger.type, None)


def test_log_message_info(logger: Logger) -> None:
    """ Tests the log of an info message of the logger """
    logger.info("my info message")


def test_log_message_success(logger: Logger) -> None:
    """ Tests the log of an success message of the logger """
    logger.success("my success message")


def test_log_message_warning(logger: Logger) -> None:
    """ Tests the log of an warning message of the logger """
    logger.warning("my warning message")


def test_log_message_error(logger: Logger) -> None:
    """ Tests the log of an error message of the logger """
    logger.error("my error message")
# --- [/TESTS] --- #
