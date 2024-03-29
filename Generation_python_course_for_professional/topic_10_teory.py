class GenerateInts:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


def generate_ints(n):
    for num in range(n):
        yield num


class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1


def counter(low, high):
    for num in range(low, high + 1):
        yield num


class EvenNumbers:
    def __init__(self, begin):
        self.begin = begin + begin % 2

    def __iter__(self):
        return self

    def __next__(self):
        value = self.begin
        self.begin += 2
        return value


def even_numbers(begin):
    begin += begin % 2
    while True:
        yield begin
        begin += 2


class StringWrapper:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.text):
            raise StopIteration
        return self.symbol + self.text[self.index] + self.symbol


def string_wrapper(text, symbol):
    for char in text:
        yield symbol + char + symbol


class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value


def factorials():
    value = 1
    index = 1
    while True:
        yield value
        index += 1
        value *= index


def simple_sequence():
    n = 1
    while True:
        for _ in range(n):
            yield n
        n += 1


if __name__ == '__main__':
    generator = simple_sequence()
    print(*[next(generator) for _ in range(10)])
    pass
