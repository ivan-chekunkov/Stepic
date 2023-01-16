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


def convert(string: str) -> str:
    flag_lower, flag_upper = 0, 0
    for char in string:
        if char.isalpha():
            if char.isupper():
                flag_upper += 1
            else:
                flag_lower += 1
    if flag_lower >= flag_upper:
        return string.lower()
    else:
        return string.upper()


def filter_anagrams(word: str, words: list) -> list:
    result = []
    for word_in_list in words:
        if sorted(word_in_list) == sorted(word):
            result.append(word_in_list)
    return result


def likes(names: list) -> str:
    if len(names) == 0:
        return f'Никто не оценил данную запись'
    if len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    if len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    if len(names) > 3:
        return (f'{names[0]}, {names[1]} и {len(names)-2} '
                f'других оценили данную запись')
    return 'Ошибка значения'
