import datetime


def startOfLocalDay(date):
    """Returns the midnight at the start of a given day

    Args:
        date (datetime): a timezone-aware datetime object

    Returns:
        datetime: the 0:00 midnight at the start of that day
    """

    dayStart = date.replace(hour=0, minute=0, second=0, microsecond=0)

    return dayStart


def endOfLocalDay(date):
    """Returns one second before midnight at the end of a given day

    Args:
        date (datetime): a timezone-aware datetime object

    Returns:
        datetime: the 23:59:59 at the end of that day
    """

    dayEnd = date.replace(hour=23, minute=59, second=59, microsecond=999999)

    return dayEnd
