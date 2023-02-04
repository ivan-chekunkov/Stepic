import os
from datetime import date, datetime, time, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_3/'


def get_date_range(start: date, end: date) -> list:
    result = []
    for i in range(start.toordinal(), end.toordinal()+1):
        result.append(date.fromordinal(i))
    return result


def saturdays_between_two_dates(start: date, end: date):
    if start > end:
        start, end = end, start
    result = 0
    for i in range(start.toordinal(), end.toordinal()+1):
        if date.fromordinal(i).weekday() == 5:
            result += 1
    return result


def sorted_dates():
    dates = [date.fromisoformat(input()) for _ in range(int(input()))]
    sorted_dates = sorted(dates)
    for one_dates in sorted_dates:
        print(one_dates.strftime('%d/%m/%Y'))


def print_good_dates(dates: list[date]):
    format_date = '%B %d, %Y'
    sorted_dates = sorted(dates)
    for one_date in sorted_dates:
        if one_date.year == 1992 and one_date.day + one_date.month == 29:
            print(one_date.strftime(format_date))


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False
