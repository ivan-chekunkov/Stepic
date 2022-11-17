import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_18/'


def number_of_lines_in_the_file():
    name = input()
    with open(FILES_DIR + name, 'r') as file:
        lines = file.readlines()
        print(len(lines))


def total_cost():
    with open(FILES_DIR + 'ledger.txt', 'r') as file:
        lines = file.readlines()
        summary = 0
        for line in lines:
            coast = int(line.rstrip('\n')[1:])
            summary += coast
        print(f'${summary}')


def goooood_students():
    with open(FILES_DIR + 'grades.txt', 'r') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            _, *scores = line.rstrip('\n').split()
            scores = list(map(int, scores))
            for score in scores:
                if score < 65:
                    break
            else:
                result += 1
        print(result)


def the_longest_word_in_the_file():
    with open(FILES_DIR + 'words.txt', 'r') as file:
        line = file.read()
        words = line.split()
        max_lenth = 0
        for word in words:
            if len(word) > max_lenth:
                max_lenth = len(word)
        for word in words:
            if len(word) == max_lenth:
                print(word)


def tail_of_a_file():
    name = input()
    with open(FILES_DIR + name, 'r') as file:
        lines = file.readlines()
        if len(lines) < 10:
            for line in lines:
                print(line.rstrip())
        else:
            for index in range(len(lines) - 10, len(lines)):
                print(lines[index].rstrip())


def forbidden_words():
    with open(FILES_DIR + 'forbidden_words.txt', 'r') as file:
        forbidden_words = file.read().split()
    with open(FILES_DIR + 'stepik.txt', 'r') as file:
        text = file.read()
        for word in forbidden_words:
            text = re.sub(word, "*" * len(word), text, flags=re.I | re.M)
        print(text)


def transliteration():
    translate_dict = {
        'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v',
        'м': 'm', 'ч': 'ch',
        'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh',
        'е': 'e', 'п': 'p', 'ъ': '*',
        'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z',
        'т': 't', 'э': 'je',
        'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
        'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V',
        'М': 'M', 'Ч': 'Ch',
        'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh',
        'Е': 'E', 'П': 'P', 'Ъ': '*',
        'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z',
        'Т': 'T', 'Э': 'Je',
        'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
    }
    with open(FILES_DIR + 'cyrillic.txt', 'r', encoding='UTF-8') as file:
        text = file.read()
    result = ''
    for char in text:
        result += translate_dict.get(char, char)
    with open(FILES_DIR + 'transliteration.txt', 'w',
              encoding='UTF-8') as file:
        file.write(result)


def missed_comments():
    with open(FILES_DIR + 'func.txt', 'r') as file:
        lines = file.readlines()
        there_is_comment = False
        best_team = True
        for line in lines:
            if line.startswith('#'):
                there_is_comment = True
                continue
            if line.startswith('def ') and there_is_comment:
                there_is_comment = False
                continue
            if line.startswith('def '):
                name = line[3:].split('(')[0]
                print(name)
                best_team = False
        if best_team:
            print('Best Programming Team')


if __name__ == '__main__':
    missed_comments()
    # transliteration()
    # forbidden_words()
    # tail_of_a_file()
    # the_longest_word_in_the_file()
    # goooood_students()
    # total_cost()
    # number_of_lines_in_the_file()
    pass
