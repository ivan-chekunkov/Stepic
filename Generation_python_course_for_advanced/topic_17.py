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
        for i in range(len(lines)-1, -1, -1):
            line = lines[i]
            print(line, end='')
