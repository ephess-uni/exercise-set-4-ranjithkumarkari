try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<

from datetime import datetime

def get_shutdown_events(logfile):
    shutdown_events = []
    with open(logfile, 'r') as file:
        for line in file:
            if "Shutdown initiated" in line:
                timestamp_str = line.split()[1]  # Extracting timestamp string
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")
                shutdown_events.append((timestamp, line.strip()))
    return shutdown_events

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
