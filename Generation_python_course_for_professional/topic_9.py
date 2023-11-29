import functools
import sys
import string
from datetime import date, datetime
from functools import lru_cache


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


def zip_longest(*args, fill=None):
    len_max_list = len(max(args, key=lambda x: len(x)))
    [arg.extend((len_max_list - len(arg)) * (fill,)) for arg in args]
    return list(zip(*args))


def unusual_sorting():
    text = input()
    sotr_text = sorted(text)
    sotr_text = sorted(
        text,
        key=lambda x: (
            not x.islower(),
            not x.isupper(),
            x.isdigit() and (int(x) % 2 == 0),
            x,
        ),
    )
    print("".join(sotr_text))


def hash_as_key(objects):
    result = {}
    for object in objects:
        hash_obj = hash(object)
        temp = result.get(hash_obj)
        if temp:
            if isinstance(temp, list):
                temp.append(object)
                result[hash_obj] = temp
                continue
            result[hash_obj] = [temp, object]
            continue
        result[hash_obj] = object
    return result


def collections():
    text = eval(input())
    if type(text) is list:
        print(text[-1])
    if type(text) is set:
        print(len(text))
    if type(text) is tuple:
        print(text[0])


def mathematical_expressions():
    print(max(map(eval, sys.stdin.readlines())))


def minimum_and_maximum():
    string = input()
    min_num, max_num = input().split()
    pattern_min = (
        "Минимальное значение функции {} на отрезке [{}; {}] равно {}"
    )
    pattern_max = (
        "Максимальное значение функции {} на отрезке [{}; {}] равно {}"
    )
    result_min = min(
        eval(string.replace("x", "(" + str(index) + ")"))
        for index in range(int(min_num), int(max_num) + 1)
    )
    result_max = max(
        eval(string.replace("x", "(" + str(index) + ")"))
        for index in range(int(min_num), int(max_num) + 1)
    )
    print(pattern_min.format(string, min_num, max_num, result_min))
    print(pattern_max.format(string, min_num, max_num, result_max))


def print_operation_table(operation, rows, cols):
    for n in range(1, rows + 1):
        for m in range(1, cols + 1):
            print(operation(n, m), end=" ")
        print()


def success(login):
    print(f"Привет, {login}!")


def failure(login, text):
    print(f"{login}, попробуйте снова. Ошибка: {text}")


def verification(login, password, success, failure):
    if not any(map(lambda x: x in string.ascii_letters, password)):
        failure(login, "в пароле нет ни одной буквы")
        return
    if not any(map(lambda x: x in string.ascii_uppercase, password)):
        failure(login, "в пароле нет ни одной заглавной буквы")
        return
    if not any(map(lambda x: x in string.ascii_lowercase, password)):
        failure(login, "в пароле нет ни одной строчной буквы")
        return
    if not any(map(str.isdigit, password)):
        failure(login, "в пароле нет ни одной цифры")
        return
    success(login)


def numbers_sum(elems):
    """
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """
    result = 0
    for elem in elems:
        if type(elem) in (int, float):
            result += elem
    return result


def new_print():
    old_print = print

    def print(*args, sep=" ", end="\n"):
        old_print(
            *[arg.upper() if type(arg) is str else arg for arg in args],
            sep=sep.upper(),
            end=end.upper(),
        )


def polynom(x):
    result = x**2 + 1
    if not polynom.__dict__.get("values", False):
        polynom.__dict__["values"] = set()
    polynom.__dict__["values"].add(result)
    return result


def remove_marks(text: str, marks):
    text = list(text)
    for index in range(len(text)):
        if text[index] in marks:
            text[index] = ""
    remove_marks.__dict__["count"] = remove_marks.__dict__.get("count", 0) + 1
    return "".join(text)


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


def get_digits(number: int | float) -> list[int]:
    return list(int(i) for i in str(number) if i.isdigit())


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    result: dict[str, str | int] = {}
    result["name"] = grades["name"]
    result["top_grade"] = max(grades["grades"])
    return result


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    result = [""] * len(numbers)
    for index in range(len(numbers)):
        temp_step = (index + step) % len(numbers)
        result[temp_step] = numbers[index]
    numbers[:] = result


def matrix_to_dict(
    matrix: list[list[int | float]],
) -> dict[int, list[int | float]]:
    result = {}
    for index in range(1, len(matrix) + 1):
        result[index] = matrix[index - 1]
    return result


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


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs) ** 2
        return value

    return wrapper


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if isinstance(value, str):
            return value
        raise TypeError

    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}"
        )
        value = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(value)}")
        return value

    return wrapper


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if to_the_end:
                return value + string
            return string + value

        return wrapper

    return decorator


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f"<{tag}>{value}</{tag}>"

        return wrapper

    return decorator


def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


def strip_range(start: int, end: int, char: str = "."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            result = []
            for index, el in enumerate(str(value)):
                if start <= index < end:
                    result.append(char)
                else:
                    result.append(el)
            return "".join(result)

        return wrapper

    return decorator


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, datatype):
                return value
            raise TypeError

        return wrapper

    return decorator


def takes(*datatypes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            for arg in (*args, *kwargs.values()):
                if not isinstance(arg, datatypes):
                    raise TypeError
            return value

        return wrapper

    return decorator


def add_attrs(**attrs):
    def decorator(func):
        for key, val in attrs.items():
            func.__dict__[key] = val

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


def ignore_exception(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except exceptions as err:
                print(f"Исключение {type(err).__name__} обработано")

        return wrapper

    return decorator


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    value = func(*args, **kwargs)
                    return value
                except Exception:
                    pass
            else:
                raise MaxRetriesException

        return wrapper

    return decorator


@lru_cache
def just_dima(word):
    result = list(word)
    result.sort()
    return "".join(result)


@lru_cache
def ways(n):
    if n <= 3:
        return 1
    if n == 4:
        return 2
    return ways(n - 1) + ways(n - 3) + ways(n - 4)


if __name__ == "__main__":
    for word in sys.stdin.readlines():
        result = just_dima(word.strip("\n"))
        print(result)
    # func2()
    # print(my_pow(139))
    # func1()
    # numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
    # print(custom_isinstance(numbers, (int, float)))
    # data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
    # print(is_greater(data, 10))
    # print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
    # print(convert(15))
    pass
