from textwrap import dedent
import pytest
from datetime import datetime
from src.ex_4_2 import logstamp_to_datetime


@pytest.mark.parametrize(
    'arg',
    [
        '2000-01-01T01:01:01',
        '2001-02-03T04:05:06',
    ]
)
def test___logstamp_to_datetime___returns_datetime_type(arg, feedback):
    md = dedent(
        """
        # Feedback
        This function passes multiple timestamps to your function and checks to make
        sure that your function returns a datetime type.

        If this test is failing, make sure that your function is correctly returning
        a datetime type.
        """
    )
    feedback(md)
    assert isinstance(logstamp_to_datetime(arg), datetime)


@pytest.mark.parametrize(
    'arg',
    [
        'invalid_timestamp_format',
        '2024-04-25',  # This timestamp is missing the time part
    ]
)
def test___logstamp_to_datetime___raises_value_error_for_invalid_input(arg, feedback):
    md = dedent(
        """
        # Feedback
        This test verifies that your function raises a ValueError when provided with an invalid timestamp string.
        """
    )
    feedback(md)
    with pytest.raises(ValueError):
        logstamp_to_datetime(arg)
