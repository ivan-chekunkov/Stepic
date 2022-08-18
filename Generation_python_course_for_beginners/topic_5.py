
def the_beginning_of_the_century():
    a = input()
    if a[-2] == a[-1] == '0':
        print('YES')
    else:
        print('NO')


def chess_board():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('YES')
    else:
        print('NO')


def girls_only():
    x1 = int(input())
    y1 = input()
    if y1 == 'f' and (10 <= x1 <= 15):
        print('YES')
    else:
        print('NO')


def roman_numerals():
    str = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    i = int(input())
    if 1 <= i <= 10:
        print(str[i-1])
    else:
        print('ошибка')


def yes_or_no_thats_the_question():
    i = int(input())
    if i % 2 != 0:
        print('YES')
    elif 2 <= i <= 5:
        print('NO')
    elif 6 <= i <= 20:
        print('YES')
    else:
        print('NO')


def bishops_move():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if abs(x1 - x2) == abs(y1 - y2):
        print('YES')
    else:
        print('NO')


def knights_move():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print('YES')
    else:
        print('NO')


def queens_move():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    queens_move()
    # knights_move()
    # bishops_move()
    # yes_or_no_thats_the_question()
    # roman_numerals()
    # girls_only()
    # chess_board()
    # the_beginning_of_the_century()
    pass
