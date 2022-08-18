
def digit_1():
    m = input()
    s = 0
    for i in range(0, len(m)):
        s += int(m[i])
    print(s)


def digit_2():
    n = input()
    for i in range(0, len(n)):
        if n[i].isdigit():
            print('Цифра')
            break
    else:
        print('Цифр нет')


def how_many_times():
    n = input()
    s = 0
    f = 0
    for i in range(0, len(n)):
        if n[i] == '*':
            s += 1
        if n[i] == '+':
            f += 1
    print(f'Символ + встречается {f} раз')
    print(f'Символ * встречается {s} раз')


def identical_neighbors():
    n = input()
    s = n[0]
    f = 0
    for i in range(1, len(n)):
        if n[i] == s:
            f += 1
        s = n[i]
    print(f)


def vowels_and_consonants():
    n = input()
    g = 0
    s = 0
    gl = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
    sg = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    for i in range(0, len(n)):
        if gl.find(n[i]) != -1:
            g += 1
        if sg.find(n[i]) != -1:
            s += 1
    print(
        f'Количество гласных букв равно {g}\nКоличество согласных букв равно {s}')


def decimal_to_binary():
    n = int(input())
    weq = ''
    while n > 0:
        weq = weq + str(n % 2)
        n = n // 2
    for i in range(len(weq), 0, -1):
        print(weq[i - 1], end='')


def palindrome():
    n = input()
    if n == n[::-1]:
        print('YES')
    else:
        print('NO')


def two_halves():
    n = input()
    d = len(n) // 2
    if len(n) % 2 != 0:
        d += 1
    print(n[d:] + n[:d])


def capital_letters():
    n = input()
    if n == n.title():
        print('YES')
    else:
        print('NO')


def swap_case():
    n = input()
    print(n.swapcase())


def good_shade():
    n = input()
    d = n.upper()
    if 'ХОРОШ' in d:
        print('YES')
    else:
        print('NO')


def lowercase():
    n = input()
    s = 0
    for i in range(0, len(n)):
        if n[i] != n[i].upper():
            s += 1
    print(s)


def number_of_words():
    n = input()
    a = n.replace(' ', '')
    print(len(n) - len(a) + 1)


def a_minute_of_genetics():
    n = input()
    n = n.upper()
    print(f'Аденин:', n.count('А'))
    print(f'Гуанин:', n.count('Г'))
    print(f'Цитозин:', n.count('Ц'))
    print(f'Тимин:', n.count('Т'))


def very_strange_things():
    n = int(input())
    s = 0
    for _ in range(n):
        if input().count('11') >= 3:
            s += 1
    print(s)


def number_of_digits():
    n = input()
    s = 0
    for i in n:
        if i.isdigit():
            s += 1
    print(s)


def com_or_ru():
    n = input()
    if n.endswith('.com') or n.endswith('.ru'):
        print('YES')
    else:
        print('NO')


def the_most_frequent_symbol():
    s = input()
    m = 0
    w = ''
    for i in s:
        if m <= s.count(i):
            m = s.count(i)
            w = i
    print(w)


def first_and_last_occurrence():
    n = input()
    if n.count('f') == 0:
        print('NO')
    elif n.count('f') == 1:
        print(n.find('f'))
    else:
        print(n.find('f'), n.rfind('f'))


def deleting_a_fragment():
    n = input()
    print(n[:n.find('h')], n[n.rfind('h') + 1:], sep='')


def characters_in_the_range():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1, 1):
        print(chr(i), end=' ')


def a_simple_cipher():
    s = input()
    for i in s:
        print(ord(i), end=' ')


def caesar_s_cipher():
    n = int(input())
    s = input()
    res = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        res += alphabet[alphabet.find(s[i]) - n]
    print(res)


if __name__ == '__main__':
    caesar_s_cipher()
    # a_simple_cipher()
    # characters_in_the_range()
    # deleting_a_fragment()
    # first_and_last_occurrence()
    # the_most_frequent_symbol()
    # com_or_ru()
    # number_of_digits()
    # very_strange_things()
    # a_minute_of_genetics()
    # number_of_words()
    # lowercase()
    # good_shade()
    # swap_case()
    # capital_letters()
    # two_halves()
    # palindrome()
    # decimal_to_binary()
    # vowels_and_consonants()
    # identical_neighbors()
    # how_many_times()
    # digit_2()
    # digit_1()
    pass
