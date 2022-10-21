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
    return (summ / count)


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


def higher_order_functions_2():

    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def filter(function, items):
        result = []
        for item in items:
            if function(item):
                result.append(item)
        return result

    def q(x):
        return x**3

    def f(x):
        if 99 < x < 1000:
            if x % 5 == 2:
                return True
        return False

    numbers = [
        1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696,
        1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912,
        537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374,
        1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232,
        182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363,
        947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175,
        959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433,
        456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127
    ]
    print(*map(q, filter(f, numbers)), sep='\n')


def higher_order_functions_3():

    def reduce(operation, items, initial_value):
        acc = initial_value
        for item in items:
            acc = operation(acc, item)
        return acc

    def f(x, y):
        return x + y**2

    numbers = [
        97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1,
        -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96,
        58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67,
        62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43,
        80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27,
        82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73
    ]
    print(reduce(f, numbers, 0), sep='\n')


def higher_order_functions_4():

    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def filter(function, items):
        result = []
        for item in items:
            if function(item):
                result.append(item)
        return result

    def f(x):
        return (9 < x < 100 or -100 < x < -9) and x % 7 == 0

    def q(x):
        return x**2

    numbers = [
        77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156,
        227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49,
        183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260,
        -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43,
        128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5,
        263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148,
        242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228,
        129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10,
        236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219,
        57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205,
        123, -105
    ]
    print(sum(map(q, filter(f, numbers))))


def func_apply(func, nums):
    result = []
    for n in nums:
        result.append(func(n))
    return result


def anonymous_functions_1():

    floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88,
              4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
    words = ['racecar', 'akinremi', 'deed', 'temidayo',
             'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
    numbers = [4, 6, 9, 23, 5]

    map_result = list(map(lambda num: round(num**2, 1), floats))
    filter_result = list(
        filter(lambda name: name == name[::-1] and len(name) > 4, words))
    reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)


def anonymous_functions_2():
    data = [['Tokyo', 35676000, 'primary'],
            ['New York', 19354922, 'nan'],
            ['Mexico City', 19028000, 'primary'],
            ['Mumbai', 18978000, 'admin'],
            ['Sao Paulo', 18845000, 'admin'],
            ['Delhi', 15926000, 'admin'],
            ['Shanghai', 14987000, 'admin'],
            ['Kolkata', 14787000, 'admin'],
            ['Los Angeles', 12815475, 'nan'],
            ['Dhaka', 12797394, 'primary'],
            ['Buenos Aires', 12795000, 'primary'],
            ['Karachi', 12130000, 'admin'],
            ['Cairo', 11893000, 'primary'],
            ['Rio de Janeiro', 11748000, 'admin'],
            ['Osaka', 11294000, 'admin'],
            ['Beijing', 11106000, 'primary'],
            ['Manila', 11100000, 'primary'],
            ['Moscow', 10452000, 'primary'],
            ['Istanbul', 10061000, 'admin'],
            ['Paris', 9904000, 'primary']]

    f = filter(lambda x: x[1] > 10000000, data)
    g = filter(lambda x: x[2] == 'primary', f)
    s = sorted(g, key=lambda x: x[0])
    r = list(map(lambda x: x[0], s))
    t = 'Cities: ' + reduce(lambda c1, c2: f'{c1}, {c2}', r)
    print(t)


def anonymous_functions_group():

    def func_1(x): return True if x % 13 == 0 or x % 19 == 0 else False

    def func_2(x): return True if x[0].lower(
    ) == 'a' and x[-1].lower() == 'a' else False

    def is_non_negative_num(x): return True if x.replace(
        '.', '').isdigit() and x.count('.') < 2 and float(x) >= 0 else False

    def is_num(x): return x.replace('.', '', 1).replace(
        '-', '', 1).isdigit() and x[1:].count('-') == 0


def anonymous_functions_3():
    words = [
        'beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse',
        'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct',
        'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow',
        'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard',
        'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday',
        'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle',
        'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday',
        'accessory', 'absorb'
    ]
    print(*filter(lambda x: len(x) == 6, sorted(words)), sep=' ')


def anonymous_functions_4():
    numbers = [
        46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100,
        36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93,
        36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
        57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6,
        4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49,
        5, 33, 60, 94, 89, 8, 36, 94, 46, 33
    ]
    print(*map(lambda x: x // 2 if x % 2 == 0 else x,
          filter(lambda x: not (x % 2 and x > 47), numbers)))
