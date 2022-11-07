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
