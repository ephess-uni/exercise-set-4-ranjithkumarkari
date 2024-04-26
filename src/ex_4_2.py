from datetime import datetime

def logstamp_to_datetime(datestr):

    if isinstance(datestr, datetime):  # Check if the input is already a datetime object
        return datestr

    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
