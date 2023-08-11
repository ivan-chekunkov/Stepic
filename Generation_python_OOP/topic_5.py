
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
