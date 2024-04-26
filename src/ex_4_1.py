""" ex_4_1.py """
import os

try:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def num_shutdowns(logfile):
    def num_shutdowns(logfile):
        """
        Count the number of shutdown events in the given log file.

        Args:
            logfile (str): The path to the log file.

        Returns:
            int: The number of shutdown events.
        """
        shutdown_events = get_shutdown_events(logfile)
        return len(shutdown_events)


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')