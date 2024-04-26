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




def time_between_shutdowns(file_path):
    try:
        # Read the log file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        shutdown_timestamps = []

        # Extract timestamps of shutdown events
        for line in lines:
            if 'Shutdown initiated' in line:
                timestamp_str = line.split()[1:3]  # Extract date and time parts
                timestamp = ' '.join(timestamp_str)  # Join date and time parts
                shutdown_timestamps.append(logstamp_to_datetime(timestamp))

        # Calculate time between shutdown events
        time_between_shutdowns = timedelta(0)
        for i in range(1, len(shutdown_timestamps)):
            time_between_shutdowns += shutdown_timestamps[i] - shutdown_timestamps[i - 1]

        return time_between_shutdowns
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
