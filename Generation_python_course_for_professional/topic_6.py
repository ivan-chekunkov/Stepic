import pickle
import string
from collections import defaultdict, namedtuple, OrderedDict, Counter, ChainMap
import csv
import datetime
import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + "/files_topic_6/"


def i_am_a_kind_of_translator_myself():
    translator = str.maketrans(string.ascii_letters, input() * 2)
    print(input().translate(translator))


def func_1():
    Fruit = namedtuple("Fruit", ["name", "color", "vitamins"])


def func_2():
    Game = namedtuple("Game", "name developer publisher")
    ExtendedGame = namedtuple("ExtendedGame", Game._fields + ("release_date", "price"))


Animal = namedtuple("Animal", ["name", "family", "sex", "color"])


def func_3():
    with open(file=FILES_DIR + "/data.pkl", mode="rb") as file:
        obj = pickle.load(file)
    for index, animal in enumerate(obj):
        for field, value in zip(Animal._fields, animal):
            print(f"{field}: {value}")
        if index == len(obj) - 1:
            return
        print()


def func_4():
    User = namedtuple("User", ["name", "surname", "email", "plan"])
    users = [
        User("Mary", "Griffin", "sonnen@yahoo.com", "Basic"),
        User("Brenda", "Young", "retoh@outlook.com", "Silver"),
        User("Kathleen", "Lyons", "balchen@att.net", "Gold"),
        User("Pamela", "Hicks", "corrada@sbcglobal.net", "Silver"),
        User("William", "Townsend", "kosact@verizon.net", "Gold"),
        User("Clayton", "Morris", "berserk@yahoo.com", "Silver"),
        User("Dorothy", "Dennis", "sequin@live.com", "Gold"),
        User("Tyler", "Walker", "noahb@comcast.net", "Basic"),
        User("Joseph", "Moore", "ylchang@sbcglobal.net", "Silver"),
        User("Kenneth", "Richardson", "tbusch@me.com", "Bronze"),
        User("Stephanie", "Bush", "neuffer@live.com", "Gold"),
        User("Gregory", "Hughes", "juliano@att.net", "Basic"),
        User("Tracy", "Wallace", "sblack@me.com", "Silver"),
        User("Russell", "Smith", "isaacson@comcast.net", "Bronze"),
        User("Megan", "Patterson", "hoangle@outlook.com", "Basic"),
    ]
    STATUS = {"Gold": 1, "Silver": 2, "Bronze": 3, "Basic": 4}
    sorted_users = sorted(users, key=lambda x: (STATUS[x.plan], x.email))
    for user in sorted_users:
        print(f"{user.name} {user.surname}")
        print(f"  Email: {user.email}")
        print(f"  Plan: {user.plan}")
        print()


Meeting = namedtuple("Meeting", ["name", "data"])


def who_are_you_i_didnt_call_you():
    with open(file=FILES_DIR + "/meetings.csv", mode="r", encoding="UTF-8") as file:
        data = csv.DictReader(file)
        meetings = []
        pattern = "%d.%m.%Y.%H:%M"
        for line in data:
            name = line["surname"] + " " + line["name"]
            data_time = line["meeting_date"] + "." + line["meeting_time"]
            data_meeting = datetime.datetime.strptime(data_time, pattern)
            meetings.append(Meeting(name, data_meeting))
        meetings.sort(key=lambda x: x[1])
        for meeting in meetings:
            print(meeting.name)


def func_5():
    data = [
        ("Books", 1343),
        ("Books", 1166),
        ("Merch", 616),
        ("Courses", 966),
        ("Merch", 1145),
        ("Courses", 1061),
        ("Books", 848),
        ("Courses", 964),
        ("Tutorials", 832),
        ("Merch", 642),
        ("Books", 815),
        ("Tutorials", 1041),
        ("Books", 1218),
        ("Tutorials", 880),
        ("Books", 1003),
        ("Merch", 951),
        ("Books", 920),
        ("Merch", 729),
        ("Tutorials", 977),
        ("Books", 656),
    ]
    data_defdict = defaultdict(int)
    for elem in data:
        data_defdict[elem[0]] += elem[1]
    for elem in sorted(data_defdict):
        print(f"{elem}: ${data_defdict[elem]}")


def func_6():
    staff = [
        ("Sales", "Robert Barnes"),
        ("Developing", "Thomas Porter"),
        ("Accounting", "James Wilkins"),
        ("Sales", "Connie Reid"),
        ("Accounting", "Brenda Davis"),
        ("Developing", "Miguel Norris"),
        ("Accounting", "Linda Hudson"),
        ("Developing", "Deborah George"),
        ("Developing", "Nicole Watts"),
        ("Marketing", "Billy Lloyd"),
        ("Sales", "Charlotte Cox"),
        ("Marketing", "Bernice Ramos"),
        ("Sales", "Jose Taylor"),
        ("Sales", "Katie Warner"),
        ("Accounting", "Steven Diaz"),
        ("Accounting", "Kimberly Reynolds"),
        ("Accounting", "John Watts"),
        ("Accounting", "Dale Houston"),
        ("Developing", "Arlene Gibson"),
        ("Marketing", "Joyce Lawrence"),
        ("Accounting", "Rosemary Garcia"),
        ("Marketing", "Ralph Morgan"),
        ("Marketing", "Sam Davis"),
        ("Marketing", "Gail Hill"),
        ("Accounting", "Michelle Wright"),
        ("Accounting", "Casey Jenkins"),
        ("Sales", "Evelyn Martin"),
        ("Accounting", "Aaron Ferguson"),
        ("Marketing", "Andrew Clark"),
        ("Marketing", "John Gonzalez"),
        ("Developing", "Wilma Woods"),
        ("Sales", "Marie Cooper"),
        ("Accounting", "Kay Scott"),
        ("Sales", "Gladys Taylor"),
        ("Accounting", "Ann Bell"),
        ("Accounting", "Craig Wood"),
        ("Accounting", "Gloria Higgins"),
        ("Marketing", "Mario Reynolds"),
        ("Marketing", "Helen Taylor"),
        ("Marketing", "Mary King"),
        ("Accounting", "Jane Jackson"),
        ("Marketing", "Carol Peters"),
        ("Sales", "Alicia Mendoza"),
        ("Accounting", "Edna Cunningham"),
        ("Developing", "Joyce Rivera"),
        ("Sales", "Joseph Lee"),
        ("Sales", "John White"),
        ("Marketing", "Charles Bailey"),
        ("Sales", "Chester Fernandez"),
        ("Sales", "John Washington"),
    ]
    data_defdict = defaultdict(int)
    for elem in staff:
        data_defdict[elem[0]] += 1
    for elem in sorted(data_defdict):
        print(f"{elem}: {data_defdict[elem]}")


def func_7():
    staff_broken = [
        ("Developing", "Miguel Norris"),
        ("Sales", "Connie Reid"),
        ("Sales", "Joseph Lee"),
        ("Marketing", "Carol Peters"),
        ("Accounting", "Linda Hudson"),
        ("Accounting", "Ann Bell"),
        ("Marketing", "Ralph Morgan"),
        ("Accounting", "Gloria Higgins"),
        ("Developing", "Wilma Woods"),
        ("Developing", "Wilma Woods"),
        ("Marketing", "Bernice Ramos"),
        ("Marketing", "Joyce Lawrence"),
        ("Accounting", "Craig Wood"),
        ("Developing", "Nicole Watts"),
        ("Sales", "Jose Taylor"),
        ("Accounting", "Linda Hudson"),
        ("Accounting", "Edna Cunningham"),
        ("Sales", "Jose Taylor"),
        ("Marketing", "Helen Taylor"),
        ("Accounting", "Kimberly Reynolds"),
        ("Marketing", "Mary King"),
        ("Sales", "Joseph Lee"),
        ("Accounting", "Gloria Higgins"),
        ("Marketing", "Andrew Clark"),
        ("Accounting", "John Watts"),
        ("Accounting", "Rosemary Garcia"),
        ("Accounting", "Steven Diaz"),
        ("Marketing", "Mary King"),
        ("Sales", "Gladys Taylor"),
        ("Developing", "Thomas Porter"),
        ("Accounting", "Brenda Davis"),
        ("Sales", "Connie Reid"),
        ("Sales", "Alicia Mendoza"),
        ("Marketing", "Mario Reynolds"),
        ("Sales", "John White"),
        ("Developing", "Joyce Rivera"),
        ("Accounting", "Steven Diaz"),
        ("Developing", "Arlene Gibson"),
        ("Sales", "Robert Barnes"),
        ("Sales", "Charlotte Cox"),
        ("Accounting", "Craig Wood"),
        ("Marketing", "Carol Peters"),
        ("Marketing", "Ralph Morgan"),
        ("Accounting", "Kay Scott"),
        ("Sales", "Evelyn Martin"),
        ("Marketing", "Billy Lloyd"),
        ("Sales", "Gladys Taylor"),
        ("Developing", "Deborah George"),
        ("Sales", "Charlotte Cox"),
        ("Marketing", "Sam Davis"),
        ("Sales", "John White"),
        ("Sales", "Marie Cooper"),
        ("Marketing", "John Gonzalez"),
        ("Sales", "John Washington"),
        ("Sales", "Chester Fernandez"),
        ("Sales", "Alicia Mendoza"),
        ("Sales", "Katie Warner"),
        ("Accounting", "Jane Jackson"),
        ("Sales", "Chester Fernandez"),
        ("Marketing", "Charles Bailey"),
        ("Marketing", "Gail Hill"),
        ("Accounting", "Casey Jenkins"),
        ("Accounting", "James Wilkins"),
        ("Accounting", "Casey Jenkins"),
        ("Marketing", "Mario Reynolds"),
        ("Accounting", "Aaron Ferguson"),
        ("Accounting", "Kimberly Reynolds"),
        ("Sales", "Robert Barnes"),
        ("Accounting", "Aaron Ferguson"),
        ("Accounting", "Jane Jackson"),
        ("Developing", "Deborah George"),
        ("Accounting", "Michelle Wright"),
        ("Accounting", "Dale Houston"),
    ]
    data_defdict = defaultdict(set)
    for i in staff_broken:
        data_defdict[i[0]].add(i[1])
    for key, val in sorted(data_defdict.items()):
        print(f"{key}: ", end="")
        print(", ".join(sorted(val)))


def wins(pairs) -> defaultdict:
    result = defaultdict(set)
    for win, nowin in pairs:
        result[win].add(nowin)
    return result


def flip_dict(dict_of_lists: dict) -> defaultdict:
    result = defaultdict(list)
    for key, val in dict_of_lists.items():
        for elem in val:
            result[elem].append(key)
    return result


def best_sender(messages: list, senders: list) -> str:
    count_words: defaultdict = defaultdict(int)
    for index in range(len(senders)):
        count_words[senders[index]] += len(messages[index].split())
    sorted_words = sorted(count_words.items(), key=lambda x: (x[1], x[0]), reverse=True)
    result = sorted_words[0]
    return result[0]


def func_8():
    data = OrderedDict(
        {
            "Name": "Брусника",
            "IsNetObject": "да",
            "OperatingCompany": "Брусника",
            "TypeObject": "кафе",
            "AdmArea": "Центральный административный округ",
            "District": "район Арбат",
            "Address": "город Москва, переулок Сивцев Вражек, дом 6/2",
            "SeatsCount": "10",
        }
    )
    print(OrderedDict(reversed(data.items())))


def func_9():
    data = OrderedDict(
        {
            "Name": "Брусника",
            "IsNetObject": "да",
            "OperatingCompany": "Брусника",
            "TypeObject": "кафе",
            "AdmArea": "Центральный административный округ",
            "District": "район Арбат",
            "Address": "город Москва, переулок Сивцев Вражек, дом 6/2",
            "SeatsCount": "10",
        }
    )
    print(OrderedDict(data.popitem(last=i % 2) for i in range(len(data))))


def func10():
    data = OrderedDict(
        {
            "Law & Order": 1990,
            "The Practice": 1997,
            "Six Feet Under": 2001,
            "Joan of Arcadia": 2003,
            "The West Wing": 1999,
            "Deadwood": 2004,
            "The Sopranos": 1999,
            "Boston Legal": 2004,
            "ER": 1994,
            "Friday Night Lights": 2006,
            "24": 2001,
            "Heroes": 2006,
            "Lost": 2004,
            "Dexter": 2006,
            "Damages": 2007,
            "Big Love": 2006,
            "House": 2004,
            "Downton Abbey": 2010,
            "Grey's Anatomy": 2005,
            "Homeland": 2011,
            "Breaking Bad": 2008,
            "Game of Thrones": 2011,
            "CSI: Crime Scene Investigations": 2000,
            "Boardwalk Empire": 2010,
            "True Blood": 2008,
            "House of Cards": 2013,
            "True Detective": 2014,
        }
    )
    data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
    data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)
    print(data.sorted_values(reverse=True))


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False):
    if by_values:
        order = sorted(ordered_dict, key=lambda x: ordered_dict.get(x))
    else:
        order = sorted(ordered_dict, key=lambda x: x)
    for key in order:
        ordered_dict.move_to_end(key)


def count_occurences(word, words):
    counter = Counter(map(str.lower, words.split()))
    return counter[word.lower()]


def and_how_much_does_the_course_cost():
    def sum_unicode(word):
        result = 0
        for char in word.replace(" ", ""):
            result += ord(char)
        return result

    words = input().split(",")
    counter = Counter(words)
    max_just = len(max(counter, key=lambda x: len(x)))
    for key in sorted(counter):
        val = counter[key]
        sum_chars = sum_unicode(key)
        print(key.ljust(max_just), end="")
        print(f": {sum_chars} UC x {val} = {val * sum_chars} UC")


def the_zen_of_python():
    with open(FILES_DIR + "pythonzen.txt", mode="r", encoding="UTF-8") as file:
        text = file.read()
        chars = []
        for char in text:
            if char.isalpha():
                chars.append(char.lower())
    counter = Counter(chars)
    for key in sorted(counter):
        print(f"{key}: {counter[key]}")

    # 6.1 done
    # 6.2 done
    # 6.3 done
    # 6.4 done
    # 6.5 done
    # 6.6 done
    # 6.7 done


def zoo():
    with open("zoo.json", "r", encoding="utf-8") as file:
        zoopark = ChainMap(*json.load(file))
    count_zoo = 0
    for count in zoopark.values():
        count_zoo += count
    print(count_zoo)


if __name__ == "__main__":
    zoo()
    # the_zen_of_python()
    # and_how_much_does_the_course_cost()
    # print(count_occurences(
    #     'python', 'Python Conferences python training python events')
    # )
    # data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
    # custom_sort(data, by_values=True)
    # func10()
    # func_9()
    # func_8()
    # messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
    # senders = ['Bob', 'Charlie']
    # print(best_sender(messages, senders))
    # print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
    # result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'),
    #               ('Артур', 'Анри'), ('Артур', 'Дима')])
    # for winner, losers in sorted(result.items()):
    #     print(winner, '->', *sorted(losers))
    # func_7()
    # func_6()
    # func_5()
    # who_are_you_i_didnt_call_you()
    # func_4()
    # func_3()
    # func_2()
    # func_1()
    # i_am_a_kind_of_translator_myself()
    pass
