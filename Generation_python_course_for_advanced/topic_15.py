import math
from functools import reduce


def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    matr = []
    for _ in range(n):
        temp = []
        for _ in range(m):
            temp.append(value)
        matr.append(temp)
    return matr


def mean(*args):
    summ = 0
    count = 0
    for i in args:
        if type(i) in (int, float):
            summ += i
            count += 1
    if count == 0:
        return 0
    return(summ / count)


def greet(name, *args):
    result = 'Hello, '
    result += name
    for i in args:
        result += ' and '+i
    result += '!'
    return result


def print_products(*args):
    ls = [i for i in args if type(i) == str and i not in ('', ' ')]
    print(
        '\n'.join([f'{num}) {i}' for num, i in enumerate(ls, 1)])
        if ls else 'Нет продуктов'
    )


def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')


def compar_1(pair):
    return sum(pair)/len(pair)


def func_1():
    numbers = [
        (10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100),
        (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65),
        (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)
    ]
    print(min(numbers, key=compar_1))
    print(max(numbers, key=compar_1))


def compar_2(pair):
    return math.sqrt(pair[0]**2+pair[1]**2)


def func_2():
    points = [
        (-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3),
        (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)
    ]
    points.sort(key=compar_2)
    print(points)


def compar_3(pair):
    return min(pair)+max(pair)


def func_3():
    numbers = [
        (10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67),
        (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50),
        (34, 78, 65), (-5, 90, -1)
    ]
    numbers.sort(key=compar_3)
    print(numbers)


def sort_it_as_you_want():
    athletes = [
        ('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
        ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
        ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)
    ]
    num = input()

    def compar_name(pair):
        return pair[0]

    def compar_age(pair):
        return pair[1]

    def compar_lenth(pair):
        return pair[2]

    def compar_weith(pair):
        return pair[3]

    commands = {
        '1': compar_name,
        '2': compar_age,
        '3': compar_lenth,
        '4': compar_weith,
    }
    athletes.sort(key=commands[num])
    for i in athletes:
        print(*i)


def mathematical_functions():

    def f1(x):
        return x**2

    def f2(x):
        return x**3

    def f3(x):
        return x**0.5

    def f4(x):
        return abs(x)

    def f5(x):
        return math.sin(x)

    commands = {'квадрат': f1, 'куб': f2,
                'корень': f3, 'модуль': f4, 'синус': f5}
    i = int(input())
    c = input()
    print(commands[c](i))


def interesting_sorting_1():

    def f1(x):
        s = 0
        for c in x:
            s += int(c)
        return s

    mas = input().split()
    mas.sort(key=f1)
    print(*mas)


def interesting_sorting_2():

    def f1(x):
        s = 0
        for c in x:
            s += int(c)
        return s

    mas = [int(i) for i in input().split()]
    mas.sort()
    mas = [str(i) for i in mas]
    mas.sort(key=f1)
    print(*mas)


def higher_order_functions_1():

    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def f(x):
        return round(x, 2)

    numbers = [
        3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222,
        90.09873, 45.45, 314.1528, 2.71828, 1.41546
    ]
    numbers = map(f, numbers)
    print(*numbers, sep='\n')
