import math
from math import radians, cos, sin, tan


def degrees_fahrenheit():
    print(5 / 9 * (float(input()) - 32))


def an_interesting_number():
    a = int(input())
    a1 = a % 1000//100
    a2 = a % 100//10
    a3 = a % 10
    if (max(a1, a2, a3) - min(a1, a2, a3) ==
            a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3)):
        print('Число интересное')
    else:
        print('Число неинтересное')


def manhattan_distance():
    a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
    print(abs(a1 - b1) + abs(a2 - b2))


def three_cities():
    a = input()
    b = input()
    c = input()
    if len(a) < len(b) and len(a) < len(c):
        print(a)
        if len(b) > len(c):
            print(b)
        else:
            print(c)
    if len(c) < len(b) and len(c) < len(a):
        print(c)
        if len(b) > len(a):
            print(b)
        else:
            print(a)
    if len(b) < len(a) and len(b) < len(c):
        print(b)
        if len(a) > len(c):
            print(a)
        else:
            print(c)


def arithmetic_strings():
    a = len(input())
    b = len(input())
    c = len(input())
    if min(a, b, c) == a:
        mi = a
        if max(b, c) == b:
            ma, sr = b, c
        else:
            ma, sr = c, b
    elif min(a, b, c) == b:
        mi = b
        if max(a, c) == a:
            ma, sr = a, c
        else:
            ma, sr = c, a
    elif min(a, b, c) == c:
        mi = c
        if max(b, a) == b:
            ma, sr = b, a
        else:
            ma, sr = a, b
    if sr - mi == ma - sr:
        print('YES')
    else:
        print('NO')


def euclidean_distance():
    x1, y1, x2, y2 = float(input()), float(
        input()), float(input()), float(input())
    print(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))


def average_values():
    a, b = float(input()), float(input())
    print((a + b) / 2)
    print((a * b)**0.5)
    print((2 * a * b) / (a + b))
    print(((a**2 + b**2) / 2)**0.5)


def trigonometric_expression():
    x = radians(float(input()))
    print(sin(x) + cos(x) + tan(x)**2)


def floor_and_ceiling():
    x = float(input())
    print(math.ceil(x) + math.floor(x))


def the_quadratic_equation():
    a, b, c = float(input()), float(input()), float(input())
    D = b**2 - 4 * a * c
    if D < 0:
        print('Нет корней')
    elif D == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(min(x1, x2), max(x1, x2), sep='\n')


def a_regular_polygon():
    n = float(input())
    a = float(input())
    print((n * a**2) / (4 * math.tan(math.pi / n)))


if __name__ == '__main__':
    a_regular_polygon()
    # the_quadratic_equation()
    # floor_and_ceiling()
    # trigonometric_expression()
    # average_values()
    # euclidean_distance()
    # arithmetic_strings()
    # three_cities()
    # manhattan_distance()
    # an_interesting_number()
    # degrees_fahrenheit()
    pass
