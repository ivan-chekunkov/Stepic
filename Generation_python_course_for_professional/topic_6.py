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


Meeting = namedtuple('Meeting', ['name', 'data'])


def who_are_you_i_didnt_call_you():
    with open(
        file=FILES_DIR + '/meetings.csv', mode='r', encoding='UTF-8'
    ) as file:
        data = csv.DictReader(file)
        meetings = []
        pattern = '%d.%m.%Y.%H:%M'
        for line in data:
            name = line['surname'] + ' ' + line['name']
            data_time = line['meeting_date'] + '.' + line['meeting_time']
            data_meeting = datetime.datetime.strptime(data_time, pattern)
            meetings.append(Meeting(name, data_meeting))
        meetings.sort(key=lambda x: x[1])
        for meeting in meetings:
            print(meeting.name)


def func_5():
    data = [
        ('Books', 1343), ('Books', 1166), ('Merch', 616),
        ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832),
        ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003),
        ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)
    ]
    data_defdict = defaultdict(int)
    for elem in data:
        data_defdict[elem[0]] += (elem[1])
    for elem in sorted(data_defdict):
        print(f"{elem}: ${data_defdict[elem]}")


def func_6():
    staff = [
        ('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'),
        ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'),
        ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
        ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'),
        ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'),
        ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
        ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'),
        ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'),
        ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
        ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'),
        ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'),
        ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
        ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'),
        ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'),
        ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
        ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'),
        ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'),
        ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
        ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'),
        ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'),
        ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
        ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'),
        ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'),
        ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
        ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')
    ]
    data_defdict = defaultdict(int)
    for elem in staff:
        data_defdict[elem[0]] += 1
    for elem in sorted(data_defdict):
        print(f"{elem}: {data_defdict[elem]}")
