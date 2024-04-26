from datetime import datetime

def logstamp_to_datetime(datestr):
    """
    Parses the input date string in the format 'YYYY-MM-DDTHH:MM:SS' and returns a datetime.datetime object.

    Args:
        datestr (str or datetime.datetime): Input date string in the format 'YYYY-MM-DDTHH:MM:SS' or a datetime object.

    Returns:
        datetime.datetime: A datetime object representing the parsed date and time.
    """
    if isinstance(datestr, datetime):  # Check if the input is already a datetime object
        return datestr

    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')

# Example usage:
# date_str = '2014-07-03T23:31:22'
# datetime_obj = logstamp_to_datetime(date_str)
# print(datetime_obj)
