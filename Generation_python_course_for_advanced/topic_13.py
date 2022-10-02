from decimal import Decimal
from fractions import Fraction
from math import factorial, gcd


def func_1():
    num = Decimal(input())
    a = num.as_tuple().digits
    if - 1 < num < 1:
        print(max(a))
    else:
        print(min(a) + max(a))


def mathematical_expression():
    num = Decimal(input())
    result = num.exp() + num.ln() + num.log10() + num.sqrt()
    print(result)


def shorten_the_fraction():
    num_1 = int(input())
    num_2 = int(input())
    print(Fraction(num_1, num_2))


def operations_on_fractions():
    s1 = input()
    s2 = input()
    n1 = Fraction(s1)
    n2 = Fraction(s2)
    print(f'{s1} + {s2} = {n1 + n2}')
    print(f'{s1} - {s2} = {n1 - n2}')
    print(f'{s1} * {s2} = {n1 * n2}')
    print(f'{s1} / {s2} = {n1 / n2}')


def sum_of_fractions_1():
    num = int(input())
    result = Fraction(0)
    for index in range(1, num + 1):
        result += Fraction(1, index ** 2)
    print(result)


def sum_of_fractions_2():
    num = int(input())
    result = Fraction(0)
    for index in range(1, num + 1):
        result += Fraction(1, factorial(index))
    print(result)


def conjugate_numbers():
    n = int(input())
    z1 = complex(input())
    z2 = complex(input())
    print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1))


if __name__ == '__main__':
    conjugate_numbers()
    # ordered_fractions()
    # print(young_mathematician())
    # sum_of_fractions_2()
    # sum_of_fractions_1()
    # operations_on_fractions()
    # shorten_the_fraction()
    # mathematical_expression()
    # func_1()
    pass
