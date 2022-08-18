import math


def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*        *')
    print('*' * 10)
    pass


def draw_triangle():
    for i in range(1, 11):
        print('*' * i)


def draw_triangle_2(fill, base):
    for i in range(1, base+1):
        if i <= base // 2 + 1:
            print(fill * i)
        else:
            print(fill * (base - i + 1))


def print_fio(name, surname, patronymic):
    a = surname[0] + name[0] + patronymic[0]
    print(a.upper())


def print_digit_sum(num):
    s = 0
    for i in str(num):
        s += int(i)
    print(s)


def convert_to_miles(km):
    return km * 0.6214


def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


def get_factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result


def get_factors_2(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result


def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    return result


def merge(list1, list2):
    result = list2 + list1
    result.sort()
    return result


def merge_lists():
    def quick_merge(a):
        n = len(a)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    n = int(input())
    result = []
    for i in range(n):
        s = input().split()
        result = result + s
    d = []
    for i in result:
        d.append(int(i))
    print(*quick_merge(d))


def is_valid_triangle(side1, side2, side3):
    if (side1 < side3 + side2 and side3 < side1 + side2 and
            side2 < side3 + side1):
        return True
    return False


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def get_next_prime(num):
    while True:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            return num


def is_password_good(password):
    if len(password) > 7:
        if password != password.lower():
            if password != password.upper():
                if password.isalpha() == False:
                    return True
    return False


def is_one_away(word1, word2):
    if len(word1) == len(word2):
        s = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                s += 1
        if s == 1:
            return True
    return False


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


def is_valid_password(password):
    pas = password.split(':')
    if len(pas) > 3:
        return False
    if is_palindrome(pas[0]):
        if is_prime(int(pas[1])):
            if int(pas[2]) % 2 == 0:
                return True
    return False


def is_correct_bracket(text):
    s = 0
    for i in text:
        if s < 0:
            return False
        if i == '(':
            s += 1
        if i == ')':
            s -= 1
    if s == 0:
        return True
    return False


def convert_to_python_case(text):
    s = ''
    for j in range(len(text)):
        i = text[j]
        if j == 0:
            s += i.lower()
        else:
            if i.isupper():
                s += '_' + i.lower()
            else:
                s += i
    return s


def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def get_circle(radius):
    return 2 * radius * math.pi, radius ** 2 * math.pi


def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('Нет корней')
    elif D == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
    return min(x1, x2), max(x1, x2)


if __name__ == '__main__':
    print(*solve(int(input()), int(input()), int(input())))
    # print(*get_circle(float(input())))
    # print(*get_middle_point(int(input()), int(input()),
    #                         int(input()), int(input())))
    # print(convert_to_python_case(input()))
    # print(is_correct_bracket(input()))
    # print(is_valid_password(input()))
    # print(is_palindrome(input()))
    # print(is_one_away(input(), input()))
    # print(is_password_good(input()))
    # print(get_next_prime(int(input())))
    # print(is_prime(int(input())))
    # print(is_valid_triangle(int(input()), int(input()), int(input())))
    # merge_lists()
    # print(merge([int(c) for c in input().split()],
    #             [int(c) for c in input().split()]))
    # print(find_all(input(), input()))
    # print(get_factors_2(int(input())))
    # print(get_factors(int(input())))
    # print(get_days(int(input())))
    # print(convert_to_miles(int(input())))
    # print_digit_sum(int(input()))
    # print_fio(input(), input(), input())
    # draw_triangle_2(input(), int(input()))
    # draw_triangle()
    # draw_box()
    pass
