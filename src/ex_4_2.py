from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Convert a log timestamp string to a datetime object.

    Args:
        datestr (str): The timestamp string in the format 'YYYY-MM-DDTHH:MM:SS'.

    Returns:
        datetime.datetime: The datetime object corresponding to the timestamp string.
    """
    try:
        date_part = datestr.split()[0]
        return datetime.strptime(date_part, '%Y-%m-%dT%H:%M:%S')
    except IndexError:
        raise ValueError(f"Invalid time data: {datestr}. Timestamp string does not contain expected format.")
    except ValueError:
        raise ValueError(f"Invalid time data: {datestr}. Unable to parse timestamp string.")





# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    # Test date string with correct format
    test_date = '2014-07-03T23:31:22'
    print(f'{logstamp_to_datetime(test_date)=}')
