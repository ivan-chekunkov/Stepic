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
