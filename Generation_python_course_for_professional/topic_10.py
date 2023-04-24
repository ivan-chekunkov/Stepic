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
