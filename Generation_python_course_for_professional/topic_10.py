import random
from datetime import date


def four_num():
    numbers = [
        100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64,
        -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22
    ]
    n = iter(numbers)
    next(n)
    next(n)
    next(n)
    print(next(n))


def last_num():
    numbers = [
        100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22,
        -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22
    ]
    n = iter(numbers)
    a = 0
    while True:
        try:
            a = next(n)
        except:
            print(a)
            break


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def get_min_max(data):
    if not data:
        return None
    data_and_index = []
    for index, num in enumerate(data):
        data_and_index.append((index, num))
    return (min(data_and_index, key=lambda x: x[1])[0],
            max(data_and_index, key=lambda x: x[1])[0])


def get_min_max2(iterable) -> tuple[int, int] | None:
    iterable = iter(iterable)
    try:
        first_num = next(iterable)
        min_num = first_num
        max_num = first_num
    except StopIteration:
        return None
    for num in iterable:
        if num < min_num:
            min_num = num
            continue
        if num > max_num:
            max_num = num
    return min_num, max_num


def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


def is_iterator(obj):
    try:
        next(obj)
        return True
    except:
        return False


def random_numbers(left, right):
    def func():
        return random.randint(left, right)
    return iter(func, 'a')


class Repeater:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


class BoundedRepeater:
    def __init__(self, obj, times) -> None:
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times == 0:
            raise StopIteration
        self.times -= 1
        return self.obj


class Square:
    def __init__(self, n) -> None:
        self.n = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.start += 1
        if self.start > self.n:
            raise StopIteration
        return self.start ** 2


class Fibonacci:
    def __init__(self) -> None:
        self.current = 0
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.start, self.current = self.current, self.current + self.start
        return self.current


class PowerOf:
    def __init__(self, number) -> None:
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.index += 1
        return self.number ** self.index


class DictItemsIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.data_iterator = iter(data)

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        try:
            key = next(self.data_iterator)
            value = self.data[key]
            return key, value
        except:
            raise StopIteration


class CardDeck:
    def __init__(self) -> None:
        self.suits_card = ['пик', 'треф', 'бубен', 'червей']
        self.nominal_card = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                             'валет', 'дама', 'король', 'туз']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.index += 1
        if self.index == 52:
            raise StopIteration
        suit = self.index // 13
        nominal = self.index % 13
        return f'{self.nominal_card[nominal]} {self.suits_card[suit]}'


class Cycle:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.start_index = -1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.start_index += 1
        return self.iterable[self.start_index % len(self.iterable)]


class RandomNumbers:
    def __init__(self, left, right, n) -> None:
        self.left = left
        self.right = right
        self.n = n
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.index += 1
        if self.index == self.n:
            raise StopIteration
        return random.randint(self.left, self.right)


class Alphabet:
    DICT_ALPHABET = {
        'en': 'abcdefghijklmnopqrstuvwxyz',
        'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    }

    def __init__(self, language) -> None:
        self.alphabet = self.DICT_ALPHABET[language]
        self.lenth = len(self.alphabet)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.index += 1
        return self.alphabet[self.index % self.lenth]


class Xrange:
    def __init__(self, start, end, step=1) -> None:
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
        else:
            if self.start <= self.end:
                raise StopIteration
        return self.start


def simple_sequence():
    n = 1
    while True:
        for _ in range(n):
            yield n
        n += 1


def alternating_sequence(count=None):
    n = 1
    while n-1 != count:
        if n % 2 == 0:
            yield 0-n
        else:
            yield n
        n += 1


def primes(left, right):
    def is_prime(num):
        for index in range(2, num):
            if num % index == 0:
                return False
        return True
    while left <= right:
        if left == 1:
            left += 1
        if is_prime(left):
            yield left
        left += 1


def reverse(sequence):
    for index in range(len(sequence)-1, -1, -1):
        yield sequence[index]


def reverse2(sequence):
    yield from sequence[::-1]


def dates(start, count=None):
    if count == None:
        count = -1
    while count != 1 and date.toordinal(start) != 3652059:
        yield start
        data = date.toordinal(start)
        start = date.fromordinal(data + 1)
        count -= 1
    yield start


def card_deck(suit):
    suits_card = ['пик', 'треф', 'бубен', 'червей']
    nominal_card = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                    'валет', 'дама', 'король', 'туз']
    suits_card.remove(suit)
    index = 0
    while True:
        suit = (index // 13) % 3
        nominal = index % 13
        yield f'{nominal_card[nominal]} {suits_card[suit]}'
        index += 1


def matrix_by_elem(matrix):
    for elem in matrix:
        yield from elem


def func_palindromes():
    index = 1
    while True:
        num = str(index)
        if num == num[::-1]:
            yield int(num)
        index += 1


def palindromes():
    yield from func_palindromes()


def flatten(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem

    # 10.1 done
    # 10.2 done
    # 10.3 done
    # 10.4 done
    # 10.5 done


if __name__ == '__main__':
    # generator = flatten([[1, 2], [[3]], [[4], 5]])
    # print(*generator)
    # generator = palindromes()
    # print(*[next(generator) for _ in range(30)])
    # print(*matrix_by_elem([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # generator = card_deck('треф')
    # print(*[next(generator) for _ in range(60)])
    # generator = dates(date(2022, 3, 8), 5)
    # print(*generator)
    # print(*reverse2([1, 2, 3, 4, 5]))
    # print(*reverse([1, 2, 3, 4, 5]))
    # generator = primes(37, 37)
    # print(*generator)
    # generator = alternating_sequence(10)
    # print(*generator)
    # generator = simple_sequence()
    # print(*[next(generator) for _ in range(10)])
    # xrange2 = Xrange(10, 1, -1)
    # print(*xrange2)
    # en_alpha = Alphabet('en')
    # print(*[next(en_alpha) for _ in range(38)])
    # iterator = RandomNumbers(1, 100, 10)
    # print(list(next(iterator) for _ in range(10)))
    # cycle = Cycle('Hello world')
    # print(list(next(cycle) for _ in range(20)))
    # cards = CardDeck()
    # print(list(next(cards) for _ in range(52)))
    # pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
    # print(*pairs)
    # power_of_two = PowerOf(2)
    # print(list(next(power_of_two) for _ in range(20)))
    # fibonacci = Fibonacci()
    # print(list(next(fibonacci) for _ in range(20)))
    # squares = Square(10)
    # print(list(squares))
    # bee = BoundedRepeater('bee', 2)
    # print(next(bee))
    # print(next(bee))
    # bee = Repeater('bee')
    # print(next(bee))
    # print(next(random_numbers(1, 100)))
    # print(is_iterator([1, 2, 3, 4, 5]))
    # print(is_iterable('18731'))
    # print(*starmap(lambda x, y, z: x * y * z,
    #                [(1, 1, 1), (1, 1, 2), (2, 2, 3)]))
    # print(get_min_max2([6, 4, 2, 33, 19, 1]))
    # print(get_min_max([2, 3, 8, 1, 7]))
    # print(*transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), sep='\n')
    # print(*filterfalse(lambda x: x % 2 == 0, (1, 2, 3, 4, 5)))
    # last_num()
    # four_num()
    pass
