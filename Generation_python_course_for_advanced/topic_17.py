import os
import re
from random import randrange, choice

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_17/'


def random_string():
    file = open(FILES_DIR + 'lines.txt', mode='r', encoding='UTF-8')
    lines = file.readlines()
    file.close()
    zerno = randrange(len(lines))
    print(lines[zerno])


def the_sum_of_two_is_1():
    text = open(FILES_DIR + 'numbers.txt')
    count = 0
    for num in text:
        num.rstrip()
        count += int(num)
    print(count)
    text.close()


def the_sum_of_two_is_2():
    text = open(FILES_DIR + 'nums.txt')
    sum = 0
    nums = text.read().split()
    for num in nums:
        sum += int(num)
    print(sum)

    text.close()


def total_cost():
    text = open(FILES_DIR + 'prices.txt')
    sum = 0
    lines = text.readlines()
    for line in lines:
        price = line.split('\t')
        sum += int(price[-1]) * int(price[-2])
    print(sum)
    text.close()


def flipping_a_line():
    with open(FILES_DIR + 'text.txt') as file:
        print(file.read()[::-1])


def reverse_order():
    with open(FILES_DIR + 'data.txt') as file:
        lines = file.readlines()
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            print(line, end='')


def long_lines():
    with open(FILES_DIR + 'lines2.txt') as fil:
        lines = fil.readlines()
        lenth = len(max(lines, key=len))
        for line in lines:
            if len(line) == lenth:
                print(line, end='')


def the_sum_of_the_numbers_in_the_rows():
    with open(FILES_DIR + 'numbers2.txt') as fil:
        lines = fil.readlines()
        for line in lines:
            print(sum([int(y) for y in line.split()]))


def the_sum_of_the_numbers_in_the_file():
    with open(FILES_DIR + 'nums2.txt') as file:
        text = file.read()
    print(sum(map(int, re.findall(r'\d+', text))))


def file_statistics():
    with open(FILES_DIR + 'file.txt') as file:
        lines = file.readlines()
        c_lines = len(lines)
        c_letters = 0
        c_words = 0
        for line in lines:
            line_m = list(i.rstrip() for i in line.split())
            for word in line_m:
                c_words += 1
                for char in word:
                    if char.isalpha():
                        c_letters += 1
    print('Input file contains:')
    print(f'{c_letters} letters')
    print(f'{c_words} words')
    print(f'{c_lines} lines')


def random_name_and_surname():
    with open(FILES_DIR + 'first_names.txt') as file:
        first_names = list(map(str.strip, file.read().split()))
    with open(FILES_DIR + 'last_names.txt') as file:
        last_names = list(map(str.strip, file.read().split()))
    for _ in range(3):
        print(choice(first_names), choice(last_names))


def unusual_countries():
    with open(FILES_DIR + 'population.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        title, population = line.strip().split('\t')
        if int(population) > 500000 and title[0] == 'G':
            print(title)


def read_csv():
    result = []
    with open(FILES_DIR + 'data.csv', 'r') as file:
        name_dict = file.readline().strip().split(',')
        lines = file.readlines()
        for line in lines:
            words = line.split(',')
            temp = {}
            step = 0
            for word in words:
                name = name_dict[step]
                temp[name] = word.strip()
                step += 1
            result.append(temp)
    return (result)


def random_numbers():
    with open(FILES_DIR + 'random.txt', 'w') as file:
        nums = []
        for _ in range(25):
            num = randrange(111, 777)
            nums.append(str(num)+'\n')
        file.writelines(nums)


def line_numbering():
    with open(FILES_DIR + 'input.txt', 'r') as file:
        lines = file.readlines()
    with open(FILES_DIR + 'output2.txt', 'w') as out:
        for index, line in enumerate(lines, start=1):
            out.write(f'{index}) {line}')


def a_gift_for_the_new_year():
    with open(FILES_DIR + 'class_scores.txt', 'r') as file:
        lines = file.readlines()
    with open(FILES_DIR + 'new_scores.txt', 'w') as file:
        for line in lines:
            name, score = line.split()
            score = int(score) + 5
            if score > 100:
                score = 100
            file.write(f'{name} {score}\n')


def the_riddle_by_jacques_fresco():
    with open(FILES_DIR + 'goats.txt', 'r') as file:
        lines = file.readlines()
    colors = []
    goats = {}
    goat = False
    count_goats = 0
    for line in lines:
        line = line.rstrip('\n')
        if line == 'COLOURS':
            continue
        if line == 'GOATS':
            goat = True
            continue
        if goat:
            goats[line] = goats.get(line, 0) + 1
            count_goats += 1
            continue
        colors.append(line)
    goats = dict(sorted(goats.items(), key=lambda x: x[0]))
    with open(FILES_DIR + 'answer.txt', 'w') as file:
        for key, value in goats.items():
            if int(value / count_goats * 100) > 7:
                file.write(f'{key}\n')


def file_concatenation():
    with open(FILES_DIR + 'output_all_files.txt', 'w') as file:
        for _ in range(int(input())):
            name = input()
            with open(name, 'r') as text:
                lines = text.readlines()
            file.writelines(lines)


def log_file():
    with open(FILES_DIR + 'logfile.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    with open(FILES_DIR + 'output.txt', 'w') as file:
        for line in lines:
            name, data_in, data_out = line.rstrip('\n').split(', ')
            minutes_in = int(data_in[:2]) * 60 + int(data_in[3:])
            minutes_out = int(data_out[:2]) * 60 + int(data_out[3:])
            if minutes_out - minutes_in >= 60:
                file.write(f'{name}\n')


if __name__ == '__main__':
    file_concatenation()
    # line_numbering()
    # random_numbers()
    # print(read_csv())
    # unusual_countries()
    # random_name_and_surname()
    # file_statistics()
    # the_sum_of_the_numbers_in_the_file()
    # the_sum_of_the_numbers_in_the_rows()
    # long_lines()
    # reverse_order()
    # flipping_a_line()
    # total_cost()
    # the_sum_of_two_is_2()
    # the_sum_of_two_is_1()
    # random_string()
    # log_file()
    # the_riddle_by_jacques_fresco()
    # a_gift_for_the_new_year()
    pass
