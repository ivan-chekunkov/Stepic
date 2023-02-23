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
