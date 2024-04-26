""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Return log entries where shutdowns were initiated.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - list: List of log entries where shutdowns were initiated.
    """
    # Initialize an empty list to store shutdown events
    shutdown_events = []

    # Open the log file and read its contents
    with open(logfile, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line contains the phrase "Shutdown initiated"
            if "Shutdown initiated" in line:
                # If it does, add the line to the list of shutdown events
                shutdown_events.append(line.strip())

    # Return the list of shutdown events
    return shutdown_events
    pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
