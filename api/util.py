from datetime import datetime, time


def datetimeconverter(o):
    if isinstance(o, time) or isinstance(o, datetime):
        return o.__str__()


def get_date(data):
    try:
        return datetime.strptime(data['date'], "%Y-%m-%d")
    except KeyError:
        return datetime.now().date()


def get_time(duration):
    hour = int(duration.split(":")[0])
    minute = int(duration.split(":")[1])
    return time(hour, minute)
