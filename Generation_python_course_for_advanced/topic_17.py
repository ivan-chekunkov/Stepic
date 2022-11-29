import os
from random import randrange, choice

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_17/'


def random_string():
    file = open(FILES_DIR + 'lines.txt', mode='r', encoding='UTF-8')
    lines = file.readlines()
    file.close()
    zerno = randrange(len(lines))
    print(lines[zerno])
