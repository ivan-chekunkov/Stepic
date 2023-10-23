import functools
from datetime import date, datetime


def convert(number):
    return f"{number:b}", f"{number:o}", f"{number:X}"


def non_negative_even(numbers):
    return all(map(lambda x: x % 2 == 0 and x >= 0, numbers))


def is_greater(lists: list[list], number: int) -> bool:
    return any(map(lambda x: sum(x) > number, lists))


def custom_isinstance(objects, typeinfo):
    result = 0
    for object in objects:
        if isinstance(object, typeinfo):
            result += 1
    return result


def func1():
    numbers = [
        -7724,
        5023,
        3197,
        -102,
        -4129,
        -880,
        5857,
        -2866,
        -8913,
        1195,
        9809,
        5347,
        -8071,
        903,
        3030,
        -4347,
        -3354,
        1024,
        8670,
        4210,
        -5228,
        8900,
        4823,
        -2002,
        4900,
        9520,
        -3658,
        1104,
        -9554,
        3064,
        9632,
        -8701,
        3384,
        4370,
        2034,
        7822,
        -9694,
        3347,
        7440,
        -8459,
        3238,
        -5193,
        -3381,
        5281,
        9022,
        5559,
        7593,
        -6540,
        -6204,
        -2483,
        8729,
        5810,
        -8254,
        -9846,
        -1801,
        4882,
        3838,
        -3140,
        7609,
        -3325,
        6026,
        2994,
        -1677,
        1266,
        -1893,
        -4408,
        -5722,
        -2841,
        9812,
        5837,
        -7474,
        4624,
        -664,
        6998,
        7888,
        -971,
        8810,
        3812,
        -5396,
        2593,
        512,
        -4634,
        9735,
        -3062,
        9031,
        -9300,
        3657,
        6332,
        7552,
        8125,
        -725,
        4392,
        1727,
        8194,
        -2828,
        -4314,
        -8967,
        -7912,
        -1363,
        -5957,
    ]
    index_max_num = max(enumerate(numbers), key=lambda x: x[1])
    print(index_max_num[0])


def my_pow(number):
    result = 0
    for index, num in enumerate(str(number), 1):
        result += int(num) ** index
    return result


def func2():
    names = [
        "Moana",
        "Cars",
        "Zootopia",
        "Ratatouille",
        "Coco",
        "Inside Out",
        "Finding Nemo",
        "Frozen",
    ]
    budgets = [
        150000000,
        120000000,
        150000000,
        150000000,
        180000000,
        175000000,
        94000000,
        150000000,
    ]
    box_offices = [
        643331111,
        462216280,
        1023784195,
        620702951,
        807082196,
        857611174,
        940335536,
        1280802282,
    ]
    films = sorted(zip(names, budgets, box_offices), key=lambda x: x[0])
    for film in films:
        print(f"{film[0]}: {film[2]-film[1]}$")


if __name__ == "__main__":
    func2()
    # print(my_pow(139))
    # func1()
    # numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
    # print(custom_isinstance(numbers, (int, float)))
    # data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
    # print(is_greater(data, 10))
    # print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
    # print(convert(15))
    pass


def power(degree):
    def func(x):
        return x**degree

    return func


def generator_square_polynom(a, b, c):
    def func(x):
        return a * x**2 + b * x + c

    return func


def sourcetemplate(url):
    def func(**kwargs):
        result = [
            url,
        ]
        if kwargs:
            result.append("?")
            temp = []
            for key in sorted(kwargs):
                val = kwargs[key]
                temp.append(f"{key}={val}")
            result.append("&".join(temp))
        return "".join(result)

    return func


def date_formatter(country_code):
    def func(data: date):
        country_format = {
            "ru": "%d.%m.%Y",
            "us": "%m-%d-%Y",
            "ca": "%Y-%m-%d",
            "br": "%d/%m/%Y",
            "fr": "%d.%m.%Y",
            "pt": "%d-%m-%Y",
        }
        pattern = country_format[country_code]
        return datetime.strftime(data, pattern)

    return func


def sort_priority(values, group):
    not_priority_nums = []
    index = 0
    while index < len(values):
        if values[index] in group:
            index += 1
        else:
            not_priority_nums.append(values[index])
            del values[index]
    values.sort()
    not_priority_nums.sort()
    for num in not_priority_nums:
        values.append(num)
    return values


def sort_priority2(values, group):
    def comparator(x):
        return x not in group, x

    values.sort(key=comparator)


def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return result

    return wrapper


def upper_print(func):
    def wrapper(*args, **kwargs):
        args = tuple(i.upper() if isinstance(i, str) else i for i in args)
        kwargs = dict((k, v.upper()) for k, v in kwargs.items())
        return func(*args, **kwargs)

    return wrapper


print = upper_print(print)


def do_twice(func):
    def wrapper(*args, **kwargs):
        for _ in range(2):
            result = func(*args, **kwargs)
        return result

    return wrapper


def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)

    return wrapper


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            return None, "При вызове функции произошла ошибка"
        return result, "Функция выполнилась без ошибок"

    return wrapper


def takes_positive(func):
    def wrapper(*args, **kwargs):
        val = [*args, *kwargs.values()]
        if all(map(lambda x: isinstance(x, int), val)):
            if all(map(lambda x: x > 0, val)):
                result = func(*args, **kwargs)
                return result
            else:
                raise ValueError
        else:
            raise TypeError

    return wrapper
