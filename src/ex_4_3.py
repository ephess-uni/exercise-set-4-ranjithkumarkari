import os
from datetime import timedelta

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


def time_between_shutdowns(logfile):
    """
    Calculates the amount of time between the first and last shutdown events in a log file.

    Args:
        logfile (str): The filename of the log file.

    Returns:
        datetime.timedelta: The time difference between the first and last shutdown events.
    """
    # Get shutdown events from the log file
    shutdown_events = get_shutdown_events(logfile)

    # Check if shutdown_events is empty
    if not shutdown_events:
        return timedelta()  # Return zero timedelta if no shutdown events are found

    try:
        # Convert the date field of the first shutdown event to a datetime object
        first_shutdown_timestamp = logstamp_to_datetime(shutdown_events[0])

        # Convert the date field of the last shutdown event to a datetime object
        last_shutdown_timestamp = logstamp_to_datetime(shutdown_events[-1])

        # Compute the difference in time between the two events
        time_difference = last_shutdown_timestamp - first_shutdown_timestamp

        return time_difference

    except ValueError as e:
        print(f"Error: {e}")
        return timedelta()  # Return zero timedelta if there's an error


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
