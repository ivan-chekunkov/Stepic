import re
from datetime import date
from functools import singledispatchmethod
from math import pi, sqrt
from typing import Iterable


class PiggyBank:

    def __init__(self, balance=0, volume=400):
        self.balance = balance
        self.volume = volume

    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            raise ValueError('Копилка слишком мала')
        else:
            self.balance += coins

    def remove_coins(self, coins):
        if self.balance - coins < 0:
            raise ValueError('В копилке недостаточно монет')
        else:
            self.balance -= coins


class Gun:

    def shoot(self):
        print('pif')


class User:

    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, count):
        self.friends += count


class House:

    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, count):
        self.rooms += count


class Circle:

    def __innit__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2


class Bee:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


class Gun1:

    def __init__(self):
        self.step = 1

    def shoot(self):
        if self.step % 2:
            print('pif')
        else:
            print('paf')
        self.step += 1


class Gun2:

    def __init__(self):
        self.shots = 1

    def shoot(self):
        if self.shots % 2:
            print('pif')
        else:
            print('paf')
        self.shots += 1

    def shots_count(self):
        return self.shots - 1

    def shots_reset(self):
        self.shots = 1


class Scales:

    def __init__(self):
        self.right_weight = 0
        self.left_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def get_result(self):
        if self.left_weight > self.right_weight:
            return 'Левая чаша тяжелее'
        elif self.left_weight == self.right_weight:
            return 'Весы в равновесии'
        return 'Правая чаша тяжелее'


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x**2 + self.y**2)**0.5


class Numbers:

    def __init__(self):
        self.even_nums = []
        self.odd_nums = []

    def add_number(self, number):
        if number % 2 == 0:
            self.even_nums.append(number)
        else:
            self.odd_nums.append(number)

    def get_even(self):
        return list(self.even_nums)

    def get_odd(self):
        return list(self.odd_nums)


class TextHandler:

    def __init__(self):
        self.shortest_words = []
        self.longest_words = []
        self.min_len = float('inf')
        self.max_len = 0

    def add_words(self, text):
        for word in text.split():
            if len(word) < self.min_len:
                self.shortest_words = []
                self.min_len = len(word)
            elif len(word) > self.max_len:
                self.longest_words = []
                self.max_len = len(word)
            if len(word) == self.min_len:
                self.shortest_words.append(word)
            elif len(word) == self.max_len:
                self.longest_words.append(word)

    def get_shortest_words(self):
        return self.shortest_words.copy()

    def get_longest_words(self):
        return self.longest_words.copy()


class Todo:

    def __init__(self):
        self.things = []
        self.min_priority = float('inf')
        self.max_priority = 0

    def add(self, thing, priority):
        self.things.append((thing, priority))
        self.min_priority = min(self.min_priority, priority)
        self.max_priority = max(self.max_priority, priority)

    def get_by_priority(self, n):
        return [name for name, priority in self.things if priority == n]

    def get_low_priority(self):
        return self.get_by_priority(self.min_priority)

    def get_high_priority(self):
        return self.get_by_priority(self.max_priority)


class Postman:

    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        temp = [house for st, house, _ in self.delivery_data if st == street]
        temp_set = set(temp)
        result = []
        for elem in temp:
            if elem in temp_set:
                result.append(elem)
                temp_set.discard(elem)
        return result

    def get_flats_for_house(self, street, house):
        temp = [
            ap for st, home, ap in self.delivery_data
            if st == street and home == house
        ]
        temp_set = set(temp)
        result = []
        for elem in temp:
            if elem in temp_set:
                result.append(elem)
                temp_set.discard(elem)
        return result


class Wordplay:

    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only_it_chars(self, word, chars):
        return all([True if char in chars else False for char in word])

    def not_in_word(self, word, chars):
        return not any([True if char in word else False for char in chars])

    def only(self, *args):
        return [word for word in self.words if self.only_it_chars(word, args)]

    def avoid(self, *args):
        return [word for word in self.words if self.not_in_word(word, args)]


class Knight:

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.num_horizontal = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

    def get_char(self):
        return 'N'

    def can_move(self, x, y) -> bool:
        start_x = self.num_horizontal[self.horizontal]
        start_y = self.vertical
        if not 0 < y < 9:
            return False
        if x not in self.num_horizontal:
            return False
        if abs(self.num_horizontal[x] - start_x) == 0 or abs(y - start_y) == 0:
            return False
        s = abs(self.num_horizontal[x] - start_x) + abs(y - start_y)
        if not s == 3:
            return False
        return True

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        for y in range(9, 1, -1):
            for x in self.num_horizontal.keys():
                if self.horizontal == x and self.vertical == y:
                    symbol = self.get_char()
                elif self.can_move(x, y):
                    symbol = '*'
                else:
                    symbol = '.'
                print(symbol, end='')
            print()


class Circle1:

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius**2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


class User1:

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


class HourClock:

    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not (isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(get_hours, set_hours)


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._fullname = None

    def get_fullname(self):
        if self._fullname is None:
            self._fullname = self.name + ' ' + self.surname
        return self._fullname

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)


class Person1:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


class Account:

    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)


class QuadraticPolynomial:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if (pow(self.b, 2) - 4 * self.a * self.c) < 0:
            return None
        return (-self.b -
                sqrt(pow(self.b, 2) - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def x2(self):
        if (pow(self.b, 2) - 4 * self.a * self.c) < 0:
            return None
        return (-self.b +
                sqrt(pow(self.b, 2) - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def view(self):
        answear = [
            self.a,
        ]
        answear.extend(("-", abs(self.b))) if self.b < 0 else answear.extend(
            ("+", self.b))
        answear.extend(("-", abs(self.c))) if self.c < 0 else answear.extend(
            ("+", self.c))
        return "{}x^2 {} {}x {} {}".format(*answear)

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coeffs: tuple):
        self.a, self.b, self.c = coeffs


class Color:

    def __init__(self, hexcode) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, code):
        self._hexcode = code
        self.r = int(self._hexcode[0:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:6], 16)


class Circle2:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Rectangle1:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)


class QuadraticPolynomial1:

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, data: Iterable):
        return cls(*data)

    @classmethod
    def from_str(cls, data: str):
        return cls.from_iterable(map(float, data.split()))


class Pet:
    pets = []

    def __init__(self, name) -> None:
        self.name = name
        self.__class__.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


class StrExtension:

    def __init__(self) -> None:
        pass

    @staticmethod
    def remove_vowels(text: str):
        data = ["a", "e", "i", "o", "u", "y"]
        result = []
        for char in text:
            if char.lower() not in data:
                result.append(char)
        return "".join(result)

    @staticmethod
    def leave_alpha(text: str):
        result = []
        for char in text:
            if char.isalpha():
                result.append(char)
        return "".join(result)

    @staticmethod
    def replace_all(string: str, chars: Iterable, char: str):
        for elem in chars:
            string = string.replace(elem, char)
        return string


class CaseHelper:

    @staticmethod
    def is_snake(string):
        regex = r"[a-z]+(_[a-z]*)*"
        match = re.fullmatch(regex, string)
        if match:
            return True
        return False

    @staticmethod
    def is_upper_camel(string):
        regex = r"([A-Z][a-z]*)+"
        match = re.fullmatch(regex, string)
        if match:
            return True
        return False

    @staticmethod
    def to_snake(string):
        string = re.sub(r"\B([A-Z])\B", r"_\1", string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r"_", r"", string.title())


class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(tuple)
    @staticmethod
    def tuple_process(data):
        return tuple(sorted(data))

    @process.register(list)
    @staticmethod
    def list_process(data):
        return sorted(data)

    @process.register(str)
    @staticmethod
    def str_process(data):
        return data.upper()

    @process.register(int)
    @process.register(float)
    @staticmethod
    def int_float_process(data):
        return data * 2


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_int_float_neg(data):
        return 0 - data

    @neg.register(bool)
    @staticmethod
    def _from_bool_neg(data):
        return not data


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _from_int_format(data):
        print(f"Целое число: {data}")

    @format.register(float)
    @staticmethod
    def _from_float_format(data):
        print(f"Вещественное число: {data}")

    @format.register(tuple)
    @staticmethod
    def _from_tuple_format(data):
        result = ", ".join(str(el) for el in data)
        print(f"Элементы кортежа: {result}")

    @format.register(list)
    @staticmethod
    def _from_list_format(data):
        result = ", ".join(str(el) for el in data)
        print(f"Элементы списка: {result}")

    @format.register(dict)
    @staticmethod
    def _from_dict_format(data):
        print("Пары словаря:", end=" ")
        result = ", ".join(f"({repr(key)}, {repr(val)})"
                           for key, val in data.items())
        print(result)


class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_date__init__(self, birth_date) -> None:
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str__init__(self, birth_date) -> None:
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except Exception:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_tuple_list__init__(self, birth_date) -> None:
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        return current_age(self.birth_date, date.today())


def current_age(date, today) -> int:
    age = today.year - date.year - 1
    age += (today.month, today.day) >= (date.month, date.day)
    return age
