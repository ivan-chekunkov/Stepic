import calendar
import datetime
import functools
import json
import re
import sys

from decimal import Decimal
from itertools import combinations
from typing import Counter, Iterator


def darts():
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print(min(row, col, num - row + 1, num - col + 1), end=" ")
        print()


def bracket_sequence():
    text = input()
    buffer = 0
    for char in text:
        if char == "(":
            buffer += 1
        elif char == ")" and buffer > 0:
            buffer -= 1
        else:
            return False
    return buffer == 0


def inversions(sequence: list[int]) -> int:
    result = 0
    for index_one in range(0, len(sequence)):
        for index_two in range(index_one + 1, len(sequence)):
            if sequence[index_one] > sequence[index_two]:
                result += 1
    return result


def inversions_2(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result


def pokemons():
    result = 0
    pokemons = Counter(line.rstrip() for line in sys.stdin.readlines())
    for count in pokemons.values():
        result += count - 1
    print(result)


def jsonify(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper


def coordinates():
    for line in sys.stdin.readlines():
        x, y = line.strip("()\n").split(", ")
        if (-90 <= float(x) <= 90) and (-180 <= float(y) <= 180):
            print("True")
        else:
            print("False")


def quantify(iterable, predicate):
    result = 0
    if predicate is None:
        predicate = bool
    for item in iterable:
        if predicate(item):
            result += 1
    return result


def pycon():
    year = int(input())
    month = int(input())
    target_month = calendar.monthcalendar(year, month)
    four_thursday = tuple(filter(bool, [i[3] for i in target_month]))
    answer = datetime.datetime.strftime(datetime.datetime(
        year, month, four_thursday[3]),
                                        format="%d.%m.%Y")
    print(answer)


def is_integer(string):
    try:
        int(string)
    except Exception:
        return False
    return True


def is_decimal(string):
    try:
        Decimal(string)
    except Exception:
        return False
    return True


def is_fraction(string):
    if not string:
        return False
    regex_obj = re.compile(r"-?\d+/\d*[1-9]\d*")
    return bool(regex_obj.fullmatch(string))


def intersperse(iterable, delimiter):
    flag = 0
    itt = iter(iterable)
    while True:
        try:
            num = next(itt)
        except Exception:
            break
        if flag:
            yield delimiter
        yield num
        flag = 1


def annual_return(start: int, percent: int, years: int) -> Iterator:
    for _ in range(0, years):
        yield (start := percent / 100 * start + start)


def pluck(data: dict, path: str, default: str = None):
    for key in path.split("."):
        if not isinstance(data, dict):
            return default
        data = data.get(key, False)
        if not data:
            return default
    return data


def recviz(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return

    return wrapper


if __name__ == "__main__":

    @recviz
    def fib(n):
        if n <= 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    fib(4)
    # d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
    # print(pluck(d, 'x'))
    # for value in annual_return(120000, 10, 3):
    #     print(round(value))
    # print(quantify([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x > 1))
    # coordinates()
    # pokemons()
    # print(inversions([3, 1, 4, 2]))
    # print(bracket_sequence())
    # darts()
    pass
