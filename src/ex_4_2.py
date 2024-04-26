import re
from datetime import datetime

def logstamp_to_datetime(datestr):
    """
    Convert a log timestamp string to a datetime object.

    Args:
        datestr (str): The timestamp string possibly containing additional information.

    Returns:
        datetime.datetime: The datetime object corresponding to the timestamp string.
    """
    try:
        # Use regular expressions to extract date and time components
        match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', datestr)
        if match:
            timestamp_str = match.group()
            # Parse the extracted timestamp string into a datetime object
            return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        else:
            match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', datestr)
            if match:
                timestamp_str = match.group()
                # Parse the extracted timestamp string into a datetime object
                return datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')
            else:
                raise ValueError("Timestamp string not found in the expected format")
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid time data: {datestr}. {e}")




# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    # Test date string with correct format
    test_date = 'INFO 2014-07-03T23:27:51 supybot Shutdown initiated.'
    print(f'{logstamp_to_datetime(test_date)=}')
