# coding: utf-8

__author__ = 'Andrey Maksimov <meamka@ya.ru>'
__date__ = '19.03.16'


def datetimeformat(value, format='%H:%M:%S / %d-%m-%Y'):
    """Format given `datetime.datetime` `value` to string

    :param value: `datetime.datetime` object
    :type value: `datetime.datetime`
    :param format: datetime format string
    :type format: str
    :return: formatted datetime string
    :type: str
    """
    return value.strftime(format)
