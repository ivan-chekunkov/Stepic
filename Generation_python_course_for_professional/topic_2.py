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


def test_likes() -> None:
    print(likes([]))
    print(likes(['Тимур']))
    print(likes(['Тимур', 'Артур']))
    print(likes(['Тимур', 'Артур', 'Руслан']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
    print(likes(['Тимур', 'Артур', 'Руслан',
          'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


def index_of_nearest(numbers: list, number: int) -> int:
    if not numbers:
        return -1
    result = []
    for num in numbers:
        result.append(abs(num-number))
    return result.index(min(result))


def spell(*args: str) -> dict:
    result: dict = {}
    for word in args:
        char = word[0].lower()
        if result.get(char, 0) < len(word):
            result[char] = len(word)
    return result


def choose_plural(amount: int, declensions: tuple) -> str:
    index_declensions = {
        0: (1,),
        1: (2, 3, 4,),
        2: (5, 6, 7, 8, 9, 0,),
    }
    numbers_end = int(str(amount)[-2:])
    if numbers_end in (11, 12, 13, 14,):
        return f'{amount} {declensions[2]}'
    number_end = int(str(amount)[-1])
    for key, value in index_declensions.items():
        if number_end in value:
            return f'{amount} {declensions[key]}'
    return 'Ошибка'


def get_biggest(numbers: list) -> int:
    if numbers:
        result = ''
        s_nums = list(map(str, numbers))
        lenth = len(s_nums)
        for i in range(1, lenth):
            for j in range(0, lenth-i):
                if s_nums[j] + s_nums[j + 1] > s_nums[j + 1] + s_nums[j]:
                    s_nums[j], s_nums[j + 1] = s_nums[j + 1], s_nums[j]
        for num in s_nums[::-1]:
            result += str(num)
        return int(result)
    return -1


def similar_letters() -> None:
    letters = [input() for _ in range(3)]
    if all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху', letters)):
        print('ru')
    elif all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy', letters)):
        print('en')
    else:
        print('mix')


def upheaval() -> None:
    n, x, y, a, b = [int(i) for i in input().split()]
    numbers = list(range(1, n + 1))
    numbers[x - 1:y] = reversed(numbers[x - 1:y])
    numbers[a - 1:b] = reversed(numbers[a - 1:b])
    print(*numbers)


def more_than_one() -> None:
    numbers = [int(i) for i in input().split()]
    set_numbers = sorted(set(numbers))
    for num in set_numbers:
        if numbers.count(num) > 1:
            print(num, end=' ')


def maximum_group() -> None:

    def summa(x):
        return sum(map(int, str(x)))

    count: dict = {}
    for num in range(1, int(input()) + 1):
        count[summa(num)] = count.get(summa(num), 0) + 1
    print(max(count.values()))


def translation_difficulties() -> None:
    peoples = []
    for _ in range(int(input())):
        people = input().split(', ')
        peoples.append(sorted(people))
    result = peoples[0]
    for people in peoples[1:]:
        if people == result:
            continue
        index = 0
        while index < len(result):
            if not result[index] in people:
                del result[index]
                continue
            index += 1
        if not result:
            print('Сериал снять не удастся')
            return
    if not result:
        print('Сериал снять не удастся')
    print(*result, sep=', ')


def translation_difficulties2() -> None:
    n = int(input())
    langueges = set(input().split(', '))
    for _ in range(n-1):
        langueges.intersection_update(input().split(', '))
    if langueges:
        print(*sorted(langueges), sep=', ')
    else:
        print('Сериал снять не удастся')
