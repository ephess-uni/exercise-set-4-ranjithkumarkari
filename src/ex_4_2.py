from datetime import datetime

def logstamp_to_datetime(datestr):
    """
    Convert a logstamp string to a datetime object.
    """
    if isinstance(datestr, datetime):  # Check if the input is already a datetime object
        return datestr

    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
