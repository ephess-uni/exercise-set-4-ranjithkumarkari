""" ex_4_3.py """
import os
from datetime import datetime, timedelta

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def time_between_shutdowns(logfile):
    """
    Returns the amount of time between the first and last shutdowns in the log file.

    Args:
        logfile (str): The path to the log file.

    Returns:
        datetime.timedelta: The amount of time between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)

    if not shutdown_events:  # If no shutdown events found
        return timedelta()  # Return zero timedelta

    first_shutdown_timestamp = shutdown_events[0][0]  # Extracting timestamp string
    last_shutdown_timestamp = shutdown_events[-1][0]  # Extracting timestamp string

    first_shutdown = logstamp_to_datetime(first_shutdown_timestamp)  # Convert first shutdown timestamp to datetime
    last_shutdown = logstamp_to_datetime(last_shutdown_timestamp)  # Convert last shutdown timestamp to datetime

    return last_shutdown - first_shutdown  # Compute time difference between first and last shutdowns


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
