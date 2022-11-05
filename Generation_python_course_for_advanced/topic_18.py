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
