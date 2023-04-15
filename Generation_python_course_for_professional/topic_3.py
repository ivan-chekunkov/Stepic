import calendar
import os
import time
from datetime import date, datetime, timedelta

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


def correct_dates():
    count_correct_dates = 0
    while True:
        text = input()
        if text == 'end':
            print(count_correct_dates)
            break
        day, month, year = map(int, text.split('.'))
        if is_correct(day, month, year):
            count_correct_dates += 1
            print('Корректная')
        else:
            print('Некорректная')


def cosmonauts_diary():
    path_file = FILES_DIR + '/diary.txt'
    pattern = '%d.%m.%Y; %H:%M'
    with open(path_file, 'r', encoding='UTF-8') as diary:
        diary = diary.read().split('\n\n')
    records = {}
    for note in diary:
        data, text = note.split('\n', 1)
        data = datetime.strptime(data, pattern)
        records[data] = text
    for data, text in sorted(records.items()):
        print(data.strftime(pattern))
        print(text)
        print()


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    blocked = []
    pattern = '%d.%m.%Y'
    for data in booked_dates:
        try:
            blocked.append(datetime.strptime(data, pattern).date())
        except:
            dates = get_date_range(
                *map(lambda x: datetime.strptime(x, pattern), data.split('-'))
            )
            blocked.extend(dates)
    request_data = []
    try:
        request_data.append(datetime.strptime(
            date_for_booking, pattern).date())
    except:
        dates = get_date_range(*map(
            lambda x: datetime.strptime(
                x, pattern), date_for_booking.split('-')
        )
        )
        request_data.extend(dates)
    for data in request_data:
        if data in blocked:
            return False
    return True


def num_of_sundays(year):
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=12, day=31)
    delta = (end - start).days + 1
    e = delta % 7
    r = delta // 7
    is_day = start.isoweekday()
    if 7-is_day <= e:
        r += 1
    return r


def productivity():
    pattern = '%d.%m.%Y'
    data = datetime.strptime(input(), pattern)
    print(data.strftime(pattern))
    for index in range(2, 11):
        delta = timedelta(days=index)
        data += delta
        print(data.strftime(pattern))


def adjacent_dates():
    pattern = '%d.%m.%Y'
    datas = list(map(
        lambda x: datetime.strptime(x, pattern), input().split(' ')
    ))
    result = list()
    if len(datas) == 1:
        return result
    start = datas[0]
    for index in range(1, len(datas)):
        delta = (datas[index]-start).days
        result.append(abs(delta))
        start = datas[index]
    return result


def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    datas = list(map(lambda x: datetime.strptime(x, pattern), dates))
    min_data = min(datas)
    max_data = max(datas)
    full_dates = get_date_range(min_data, max_data)
    result = []
    for data in full_dates:
        result.append(data.strftime(pattern))
    return result


def rap_by_matesha():
    pattern = '%H:%M'
    start = datetime.strptime(input(), pattern)
    end = datetime.strptime(input(), pattern)
    stop = start + timedelta(minutes=45)
    while stop <= end:
        time_start = datetime.strftime(start, pattern)
        time_stop = datetime.strftime(stop, pattern)
        print(f'{time_start} - {time_stop}')
        start = stop + timedelta(minutes=10)
        stop = start + timedelta(minutes=45)


def friday_13th():
    start = date(1, 1, 13)
    stop = date(9999, 12, 31)
    count_weekdays = {}
    while True:
        if start == stop:
            break
        if start.day != 13:
            start = start + timedelta(days=1)
            continue
        day = start.weekday()
        count_weekdays[day] = 1 + count_weekdays.get(day, 0)
        start = start + timedelta(days=1)
    for weekday in range(7):
        print(count_weekdays[weekday])


def again_i_didn_t_have_time():
    input_text = input()
    pattern = '%d.%m.%Y %H:%M'
    input_date = datetime.strptime(input_text, pattern)
    weekday = str(input_date.weekday())
    if weekday in '01234':
        start = '9:00'
        stop = '21:00'
    elif weekday in '56':
        start = '10:00'
        stop = '18:00'
    day_start = datetime.strptime(input_text[:11] + start, pattern)
    day_stop = datetime.strptime(input_text[:11] + stop, pattern)
    if day_start <= input_date < day_stop:
        print(int((day_stop - input_date).seconds/60))
    else:
        print('Магазин не работает')


def the_most_understandable_condition():
    pattern = '%d.%m.%Y'
    start_data = datetime.strptime(input(), pattern)
    end_data = datetime.strptime(input(), pattern)
    while True:
        if (start_data.day + start_data.month) % 2 == 0:
            start_data += timedelta(days=1)
        else:
            break
    while start_data <= end_data:
        if start_data.isoweekday() not in (1, 4):
            print(datetime.strftime(start_data, pattern))
        start_data += timedelta(days=3)


def employees_of_the_organization():
    min_data = datetime(9999, 12, 31)
    pattern = '%d.%m.%Y'
    min_name = ''
    count = 0
    for _ in range(int(input())):
        *name, dt = input().split()
        dt = datetime.strptime(dt, pattern)
        if dt <= min_data:
            if dt == min_data:
                count += 1
                continue
            min_data = dt
            min_name = ' '.join(name)
            count = 1
    if count > 1:
        print(datetime.strftime(min_data, pattern), count)
    else:
        print(datetime.strftime(min_data, pattern), min_name)


def employees_of_the_organization_2():
    pattern = '%d.%m.%Y'
    max_count = 0
    dict_data = {}
    for _ in range(int(input())):
        *_, dt = input().split()
        dt = datetime.strptime(dt, pattern)
        dict_data[dt] = dict_data.get(dt, 0) + 1
        if max_count < dict_data[dt]:
            max_count = dict_data[dt]
    for dt in sorted(dict_data.keys()):
        if dict_data[dt] == max_count:
            print(datetime.strftime(dt, pattern))


def employees_of_the_organization_3():
    max_data = datetime(1, 1, 1)
    min_name = 'Дни рождения не планируются'
    pattern = '%d.%m.%Y'
    data_today = datetime.strptime(input(), pattern)
    seven_days = []
    for index in range(1, 8):
        temp = data_today + timedelta(days=index)
        seven_days.append(str(temp.day) + '.' + str(temp.month))
    for _ in range(int(input())):
        *name, dt = input().split()
        dt = datetime.strptime(dt, pattern)
        if dt.month == 2 and dt.day == 29 and '1.3' in seven_days:
            dt = dt + timedelta(days=1)
        if (str(dt.day) + '.' + str(dt.month)) in seven_days:
            if dt > max_data:
                max_data = dt
                min_name = ' '.join(name)
    print(min_name)


def choose_plural(amount: int, declensions: tuple) -> str:
    index_declensions = {
        0: (1,),
        1: (2, 3, 4,),
        2: (5, 6, 7, 8, 9, 0,),
    }
    numbers_end = int(str(amount)[-2:])
    if numbers_end in (11, 12, 13, 14,):
        return f'{amount} {declensions[2]}'
    number_end = int(str(amount)[-1])
    for key, value in index_declensions.items():
        if number_end in value:
            return f'{amount} {declensions[key]}'


def fake_news():
    answear = [
        'До выхода курса осталось: {}',
        'Курс уже вышел!',
    ]
    date_course = datetime(2022, 11, 8, 12)
    pattern = '%d.%m.%Y %H:%M'
    date_input = datetime.strptime(input(), pattern)
    delta = date_course - date_input
    plural_names = [
        ('день', 'дня', 'дней'),
        ('час', 'часа', 'часов'),
        ('минута', 'минуты', 'минут'),
    ]
    if delta.days < 0:
        print(answear[1])
    elif delta.days == 0:
        if delta.seconds == 0:
            print(answear[1])
        elif delta.seconds < 3600:
            text = choose_plural(delta.seconds // 60, plural_names[2])
            print(answear[0].format(text))
        elif delta.seconds % 3600 == 0:
            text = choose_plural(delta.seconds//3600, plural_names[1])
            print(answear[0].format(text))
        else:
            hour = delta.seconds // 3600
            text = (choose_plural(hour, plural_names[1]) +
                    ' и ' + choose_plural(
                    (delta.seconds // 60) - hour * 60, plural_names[2]))
            print(answear[0].format(text))
    else:
        if delta.seconds < 3600:
            text = choose_plural(delta.days, plural_names[0])
            print(answear[0].format(text))
        else:
            text = (choose_plural(delta.days, plural_names[0]) + ' и ' +
                    choose_plural(delta.seconds // 3600, plural_names[1]))
            print(answear[0].format(text))


def calculate_it(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end-start


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def func_1(a):
    time.sleep(5)
    return a


def func_2(a):
    time.sleep(3)
    return a


def get_the_fastest_func(funcs, arg):
    min_time = 1000000000
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        time_work = end - start
        if time_work < min_time:
            min_time = time_work
            min_func = func
    return min_func


def leap_year():
    for _ in range(int(input())):
        print(calendar.isleap(int(input())))


def calendar_for_the_month():
    year, month = input().split()
    d = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    month = d[month]
    print(calendar.month(int(year), month))


def calendar_for_the_month_2():
    dt = datetime.strptime(input(), '%Y %b')
    calendar.prmonth(dt.year, dt.month)


def day_of_the_week():
    pattern = '%Y-%m-%d'
    dt = datetime.strptime(input(), pattern)
    print(dt.strftime('%A'))
