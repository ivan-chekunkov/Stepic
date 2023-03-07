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


def func_4():
    User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
    STATUS = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}
    sorted_users = sorted(users, key=lambda x: (STATUS[x.plan], x.email))
    for user in sorted_users:
        print(f'{user.name} {user.surname}')
        print(f'  Email: {user.email}')
        print(f'  Plan: {user.plan}')
        print()
