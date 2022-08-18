def only_positive():
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    s = 0
    if a1 > 0:
        s += a1
    if a2 > 0:
        s += a2
    if a3 > 0:
        s += a3
    print(s)


def a_beautiful_number():
    a = int(input())
    if 999 < a <= 9999 and (a % 7 == 0 or a % 17 == 0):
        print('YES')
    else:
        print('NO')


def triangle_inequality():
    a, b, c = int(input()), int(input()), int(input())
    if a < b + c and b < c + a and c < a + b:
        print('YES')
    else:
        print('NO')


def rook_move():
    a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
    if a1 == b1 or a2 == b2:
        print('YES')
    else:
        print('NO')


def the_kings_move():
    a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
    if ((a1 + 1 == b1 or a1 - 1 == b1 or a1 == b1) and
            (a2 + 1 == b2 or a2 - 1 == b2 or a2 == b2)):
        print('YES')
    else:
        print('NO')


def speedster_race():
    a, b = int(input()), int(input())
    if a > b:
        print('NO')
    elif a < b:
        print('YES')
    else:
        print("Don't know")


def type_of_triangle():
    a, b, c = int(input()), int(input()), int(input())
    if a != b and c != b and a != c:
        print('Разносторонний')
    elif a == b == c:
        print('Равносторонний')
    else:
        print('Равнобедренный')


def average_number():
    a, b, c = int(input()), int(input()), int(input())
    if b < a < c or b > a > c:
        print(a)
    elif a < b < c or a > b > c:
        print(b)
    elif a < c < b or a > c > b:
        print(c)


def number_of_days():
    c = int(input())
    if c == 2:
        print(28)
    elif (c < 8 and c % 2 == 1) or (c > 7 and c % 2 == 0):
        print(31)
    else:
        print(30)


def weighing_ceremony():
    c = int(input())
    if c < 60:
        print('Легкий вес')
    elif c < 64:
        print('Первый полусредний вес')
    elif c < 69:
        print('Полусредний вес')


def self_written_calculator():
    b, c = int(input()), int(input())
    ctr = input()
    if ctr == '+':
        print(b + c)
    elif ctr == '-':
        print(b - c)
    elif ctr == '/':
        if c == 0:
            print('На ноль делить нельзя!')
        else:
            print(b / c)
    elif ctr == '*':
        print(b * c)
    else:
        print('Неверная операция')


def color_mixer():
    c = input()
    b = input()
    if c == 'красный':
        if b == 'красный':
            print('красный')
        elif b == 'синий':
            print('фиолетовый')
        elif b == 'желтый':
            print('оранжевый')
        else:
            print('ошибка цвета')
    elif c == 'синий':
        if b == 'красный':
            print('фиолетовый')
        elif b == 'синий':
            print('синий')
        elif b == 'желтый':
            print('зеленый')
        else:
            print('ошибка цвета')
    elif c == 'желтый':
        if b == 'красный':
            print('оранжевый')
        elif b == 'синий':
            print('зеленый')
        elif b == 'желтый':
            print('желтый')
        else:
            print('ошибка цвета')
    else:
        print('ошибка цвета')


def roulette_wheel_colors():
    c = int(input())
    if c < 0 or c > 36:
        print('ошибка ввода')
    elif c == 0:
        print('зеленый')
    elif 0 < c < 11 or 18 < c < 29:
        if c % 2 == 0:
            print('черный')
        else:
            print('красный')
    else:
        if c % 2 != 0:
            print('черный')
        else:
            print('красный')


def intersection_of_segments():
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    if b1 < a2 or b2 < a1:
        print('пустое множество')
    elif b1 == a2:
        print(b1)
    elif b2 == a1:
        print(a1)
    elif a1 <= a2 < b1 < b2:
        print(a2, b1)
    elif a2 <= a1 < b2 < b1:
        print(a1, b2)
    elif a2 < a1 < b1 <= b2:
        print(a1, b1)
    elif a1 < a2 < b2 <= b1:
        print(a2, b2)


if __name__ == '__main__':
    intersection_of_segments()
    # roulette_wheel_colors()
    # color_mixer()
    # self_written_calculator()
    # weighing_ceremony()
    # number_of_days()
    # average_number()
    # type_of_triangle()
    # speedster_race()
    # the_kings_move()
    # rook_move()
    # triangle_inequality()
    # a_beautiful_number()
    # only_positive()
    pass
