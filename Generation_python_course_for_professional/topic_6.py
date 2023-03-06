import pickle
import string
from collections import defaultdict, namedtuple, OrderedDict, Counter
import csv
import datetime
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_6/'


def i_am_a_kind_of_translator_myself():
    translator = str.maketrans(string.ascii_letters, input() * 2)
    print(input().translate(translator))


def func_1():
    Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])


def func_2():
    Game = namedtuple('Game', 'name developer publisher')
    ExtendedGame = namedtuple(
        'ExtendedGame', Game._fields + ('release_date', 'price'))


Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])


def func_3():
    with open(file=FILES_DIR + '/data.pkl', mode='rb') as file:
        obj = pickle.load(file)
    for index, animal in enumerate(obj):
        for field, value in zip(Animal._fields, animal):
            print(f'{field}: {value}')
        if index == len(obj) - 1:
            return
        print()
