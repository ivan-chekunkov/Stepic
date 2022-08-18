def three_digit_number():
    num = int(input())
    digit3 = num % 10
    digit2 = (num // 10) % 10
    digit1 = num // 100
    print('Сумма цифр =', digit1 + digit2 + digit3)
    print('Произведение цифр =', digit1 * digit2 * digit3)


def permutation_of_digits():
    num = int(input())
    c = num % 10
    b = (num // 10) % 10
    a = num // 100
    print(a, b, c, sep='')
    print(a, c, b, sep='')
    print(b, a, c, sep='')
    print(b, c, a, sep='')
    print(c, a, b, sep='')
    print(c, b, a, sep='')


def a_four_digit_number():
    num = int(input())
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    d = num // 1000
    print('Цифра в позиции тысяч равна', d)
    print('Цифра в позиции сотен равна', c)
    print('Цифра в позиции десятков равна', b)
    print('Цифра в позиции единиц равна', a)


if __name__ == '__main__':
    a_four_digit_number()
    # permutation_of_digits()
    # three_digit_number()
    pass
