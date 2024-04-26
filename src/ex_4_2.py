from datetime import datetime


def logstamp_to_datetime(datestr):
    if isinstance(datestr, datetime):  # Check if the input is already a datetime object
        return datestr

    try:
        return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        raise ValueError(f"Invalid time data: {datestr}. Expected format: '%Y-%m-%dT%H:%M:%S'")
