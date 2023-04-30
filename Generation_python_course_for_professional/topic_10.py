import random


def four_num():
    numbers = [
        100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64,
        -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22
    ]
    n = iter(numbers)
    next(n)
    next(n)
    next(n)
    print(next(n))


def last_num():
    numbers = [
        100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22,
        -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22
    ]
    n = iter(numbers)
    a = 0
    while True:
        try:
            a = next(n)
        except:
            print(a)
            break


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def get_min_max(data):
    if not data:
        return None
    data_and_index = []
    for index, num in enumerate(data):
        data_and_index.append((index, num))
    return (min(data_and_index, key=lambda x: x[1])[0],
            max(data_and_index, key=lambda x: x[1])[0])


def get_min_max2(iterable) -> tuple[int, int] | None:
    iterable = iter(iterable)
    try:
        first_num = next(iterable)
        min_num = first_num
        max_num = first_num
    except StopIteration:
        return None
    for num in iterable:
        if num < min_num:
            min_num = num
            continue
        if num > max_num:
            max_num = num
    return min_num, max_num


def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


def is_iterator(obj):
    try:
        next(obj)
        return True
    except:
        return False


def random_numbers(left, right):
    def func():
        return random.randint(left, right)

    return iter(func, 'a')


class Repeater:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj
