import os

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
    Calculates the amount of time between the first and last shutdown events in a log file.

    Args:
        logfile (str): The filename of the log file.

    Returns:
        datetime.timedelta: The time difference between the first and last shutdown events.
    """
    # Get shutdown events from the log file
    shutdown_events = get_shutdown_events(logfile)

    # Check if shutdown_events is empty or not in the expected format
    if not shutdown_events or not isinstance(shutdown_events, list) or not isinstance(shutdown_events[0], dict):
        print("Error: Unable to retrieve shutdown events.")
        return None

    # Extract timestamps from shutdown events and convert to datetime objects
    timestamps = [logstamp_to_datetime(event["date"]) for event in shutdown_events]

    # Check if timestamps list is empty
    if not timestamps:
        print("Error: No valid timestamps found.")
        return None

    # Calculate the time difference between the first and last shutdown events
    time_difference = max(timestamps) - min(timestamps)

    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
