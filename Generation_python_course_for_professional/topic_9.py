def convert(number):
    return f'{number:b}', f'{number:o}', f'{number:X}'


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
        -7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809,
        5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900,
        4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384,
        4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281,
        9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846,
        -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266,
        -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998,
        7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031,
        -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828,
        -4314, -8967, -7912, -1363, -5957
    ]
    index_max_num = max(enumerate(numbers), key=lambda x: x[1])
    print(index_max_num[0])


def my_pow(number):
    result = 0
    for index, num in enumerate(str(number), 1):
        result += int(num)**index
    return result
