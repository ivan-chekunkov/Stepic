import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_2/'


def hide_card(card_number: str) -> str:
    card_number = card_number.replace(' ', '')
    return '*' * 12 + card_number[12:]


def same_parity(numbers: list) -> list:
    return list(filter(lambda x: (x-numbers[0]) % 2 == 0, numbers))


def is_valid(string: str) -> bool:
    if len(string) in (4, 5, 6):
        if string.isnumeric():
            return True
    return False


def print_given(*args, **kwargs) -> None:
    for arg in args:
        print(arg, type(arg))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))
