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


def similar_words() -> None:
    model_word = input()
    n = int(input())
    vowels_letters = 'ауоыиэяюёе'
    model = []
    for letter in model_word:
        if letter in vowels_letters:
            model.append(1)
        else:
            model.append(0)
    revers_model = model[::-1]
    last_vowel = revers_model.index(1)
    len_model = len(model_word) - last_vowel
    for _ in range(n):
        word = input()
        letters_word = []
        for letter in word:
            if letter in vowels_letters:
                letters_word.append(1)
            else:
                letters_word.append(0)
        if (model[:len_model] == letters_word[:len_model] and
                sum(letters_word[len_model:]) == 0):
            print(word)


def similar_words2() -> None:
    vowels = 'ауоыиэяюёе'
    model = [i for i, char in enumerate(input()) if char in vowels]
    for _ in range(int(input())):
        word = input()
        if [i for i, char in enumerate(word) if char in vowels] == model:
            print(word)


def corporate_mail() -> None:
    mails = [input() for _ in range(int(input()))]
    names = list(map(lambda x: x.split('@')[0], mails))
    names_count: dict = {}
    for name in names:
        word, count_str = name[:-1], name[-1]
        if count_str.isnumeric():
            count = int(count_str)
            if names_count.get(count) is None:
                names_count[count] = []
            names_count[count].append(word)
        else:
            if names_count.get(0) is None:
                names_count[0] = []
            names_count[0].append(name)
    for index in range(max(names_count.keys())):
        if names_count.get(index) is None:
            names_count[index] = []
    for _ in range(int(input())):
        name = input()
        is_add = False
        for key, val in sorted(names_count.items()):
            if not name in val:
                char = key
                if key == 0:
                    char = ''
                print(f'{name}{char}@beegeek.bzz')
                names_count[key].append(name)
                is_add = True
                break
        if not is_add:
            last_key = max(names_count.keys())
            names_count[last_key+1] = []
            names_count[last_key+1].append(name)
            print(f'{name}{last_key+1}@beegeek.bzz')


def files_in_s_file() -> None:

    def convert_to_byte(size: int, measure: str) -> int:
        convert_list = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
        return int(size) * (1024 ** convert_list[measure])

    def convert_to_big_byte(size: int) -> str:
        if size < 1024:
            return f'{round(size)} B'
        size /= 1024
        if size < 1024:
            return f'{round(size)} KB'
        size /= 1024
        if size < 1024:
            return f'{round(size)} MB'
        size /= 1024
        if size < 1024:
            return f'{round(size)} GB'

    data_file: list = []
    with open(file='files.txt', mode='r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            name_file, size, measure = line.split()
            name, expansion = name_file.split('.')
            data_file.append((name, expansion, convert_to_byte(size, measure)))
    exp_dict: dict = {}
    for data in data_file:
        temp = exp_dict.get(data[1], [])
        temp.append(data)
        exp_dict[data[1]] = temp
    adv_exp_dict: dict = {}
    for key, val in exp_dict.items():
        summary = 0
        for data in val:
            summary += data[2]
        adv_exp_dict[key] = (val, summary)
    sort_adv_exp_dict: dict = {}
    for data in sorted(adv_exp_dict):
        sort_adv_exp_dict[data] = adv_exp_dict[data]
    for index, items in enumerate(sort_adv_exp_dict.items()):
        key, val = items
        for file_name in sorted(val[0], key=lambda x: x[0]):
            print(f'{file_name[0]}.{file_name[1]}')
        print('-'*10)
        print(f'Summary: {convert_to_big_byte(val[1])}')
        if index != len(sort_adv_exp_dict)-1:
            print()


if __name__ == '__main__':
    files_in_s_file()
    # corporate_mail()
    # similar_words2()
    # similar_words()
    # translation_difficulties2()
    # translation_difficulties()
    # maximum_group()
    # more_than_one()
    # upheaval()
    # similar_letters()
    # print(get_biggest([61, 228, 9, 3, 11]))
    # print(choose_plural(21, ('пример', 'примера', 'примеров')))
    # print(spell('Математика', 'История', 'химия','биология', 'Информатика'))
    # print(index_of_nearest([7, 5, 4, 4, 3], 4))
    # test_likes()
    # print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
    # print(convert('pi31415!'))
    # print_given(1, [1, 2, 3], 'three', two=2)
    # print(is_valid('89651'))
    # print(same_parity([6, 0, 67, -7, 10, -20]))
    # print(hide_card('34 56 9012 56 78 1234'))
    pass
