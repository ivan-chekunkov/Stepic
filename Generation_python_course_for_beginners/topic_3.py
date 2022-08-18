def sum_of_squares_vs_square_of_sum():
    a = int(input())
    b = int(input())
    print('Квадрат суммы', a, 'и', b, 'равен', (a + b)**2)
    print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)


def a_large_number():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(a**b + c**d)


def reproduction_n_ok():
    a = input()
    n = int(a)
    nn = int(a * 2)
    nnn = int(a * 3)
    print(n + nn + nnn)


if __name__ == '__main__':
    reproduction_n_ok()
    # a_large_number()
    # sum_of_squares_vs_square_of_sum()
    pass
