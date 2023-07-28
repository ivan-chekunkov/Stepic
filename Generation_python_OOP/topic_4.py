from math import pi


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
        self.area = pi * radius ** 2


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


class Gun:
    def __init__(self):
        self.step = 1

    def shoot(self):
        if self.step % 2:
            print('pif')
        else:
            print('paf')
        self.step += 1


class Gun:
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
        return (self.x ** 2 + self.y ** 2) ** 0.5


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
        temp = [ap for st, home, ap in self.delivery_data if st ==
                street and home == house]
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
        if not word in self.words:
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
        self.num_horizontal = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
                               'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def get_char(self):
        return 'N'

    def can_move(self, x, y) -> bool:
        start_x = self.num_horizontal[self.horizontal]
        start_y = self.vertical
        if not 0 < y < 9:
            return False
        if not x in self.num_horizontal:
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
