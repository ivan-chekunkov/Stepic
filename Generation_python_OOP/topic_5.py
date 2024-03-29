import re
from decimal import Decimal


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, program_name='GenerationPy', environment='release', loglevel='verbose', version='1.0.0'):
        self.program_name = program_name
        self.environment = environment
        self.loglevel = loglevel
        self.version = version


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


def quantify(iterable, predicate):
    result = 0
    if predicate is None:
        predicate = bool
    for item in iterable:
        if predicate(item):
            result += 1
    return result


def is_integer(string):
    try:
        int(string)
    except:
        return False
    return True


def is_decimal(string):
    try:
        Decimal(string)
    except:
        return False
    return True


def is_fraction(string):
    if not string:
        return False
    regex_obj = re.compile(r'-?\d+/\d*[1-9]\d*')
    return bool(regex_obj.fullmatch(string))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented
