import os
from datetime import timedelta

try:
    from src.ex_4_3 import time_between_shutdowns
    from src.util import get_data_file_path
except ImportError:
    from ex_4_3 import time_between_shutdowns
    from util import get_data_file_path

# Use the full path to the log files for testing
TEST_DIRECTORY = os.path.join(os.getcwd(), "tests", "data")
DEFAULT_MESSAGES_FILE = os.path.join(TEST_DIRECTORY, "default_messages.log")
TEST_MESSAGES_FILE = os.path.join(TEST_DIRECTORY, "test_messages.log")


def test___time_between_shutdowns___returns_timedelta_type():
    assert isinstance(time_between_shutdowns(DEFAULT_MESSAGES_FILE), timedelta)
    assert isinstance(time_between_shutdowns(TEST_MESSAGES_FILE), timedelta)


def test___time_between_shutdowns___returns_correct_timedelta():
    assert time_between_shutdowns(DEFAULT_MESSAGES_FILE) == timedelta(seconds=211)
    assert time_between_shutdowns(TEST_MESSAGES_FILE) == timedelta(days=1, seconds=211)
