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
