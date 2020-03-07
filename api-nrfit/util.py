import base64
from datetime import datetime, time
from io import BytesIO

from flask import request


def datetimeconverter(o):
    if isinstance(o, time) or isinstance(o, datetime):
        return o.__str__()


def get_date():
    try:
        return datetime.strptime(request.json['date'], "%Y-%m-%d")
    except KeyError:
        return datetime.now().date()


def get_duration():
    duration = request.json['duration']
    hour = int(duration.split(":")[0])
    minute = int(duration.split(":")[1])
    return time(hour, minute)


def get_data(info):
    try:
        return request.json[info]
    except KeyError:
        return ""


def matplotlib_to_base64(plt):
    """
    Transform a Matplotlib graphs to a base 64 url.

    :param plt: The matplotlib graphs after plotting it.
    :return: the matplotlib graphs in base64.
    """
    try:
        figfile = BytesIO()
        plt.savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        result = 'data:image/png;base64,{}'.format(figdata_png.decode("utf-8"))
    finally:
        plt.cla()
        plt.clf()
        plt.close()

    return result
