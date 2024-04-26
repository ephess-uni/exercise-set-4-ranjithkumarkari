from datetime import timedelta
from textwrap import dedent
import pytest
from src.ex_4_3 import time_between_shutdowns


def provide_feedback(md):
    print(md)  # You can replace print with your actual feedback mechanism


@pytest.mark.parametrize(
    'logfile,feedback',
    [
        ('default_messages', provide_feedback),
        ('test_messages', provide_feedback),
    ]
)
def test___time_between_shutdowns___returns_timedelta_type(logfile, feedback):
    md = dedent(
        """
        # Feedback
        Make sure that your function returns a datetime.timedelta object.
        """
    )
    feedback(md)
    assert isinstance(time_between_shutdowns(logfile), timedelta)


@pytest.mark.parametrize(
    'logfile,expected,feedback',
    [
        ('default_messages', 'timedelta(seconds=211)', provide_feedback),
        ('test_messages', 'timedelta(days=1, seconds=211)', provide_feedback),
    ]
)
def test___time_between_shutdowns___returns_correct_timedelta(logfile, expected, feedback):
    md = dedent(
        """
        # Feedback
        Make sure that the value of the timedelta object is correct.  For the default logfile, 
        this is 211 seconds.  

        Keep in mind that your function is tested with different inputs. 
        """
    )
    feedback(md)
    assert time_between_shutdowns(logfile) == eval(expected)

