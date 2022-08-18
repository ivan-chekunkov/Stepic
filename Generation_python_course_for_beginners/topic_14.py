from math import factorial


def draw_triangle():
    n = 15
    m = 8
    for i in range(1, m + 1):
        g = (i - 1) * 2 + 1
        r = int((n - g) / 2)
        print(' ' * r + '*' * g)


def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return 1000 + (quantity - 1) * 120


def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def number_to_words(num):
    if num == 0:
        return 'ноль'
    if num == 10:
        return 'десять'
    mas1 = ['один', 'два', 'три', 'четыре', 'пять',
            'шесть', 'семь', 'восемь', 'девять']
    mas2 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
            'девятнадцать']
    mas3 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят',
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    n = str(num)
    if 11 <= num <= 19:
        return mas2[int(n[1]) - 1]
    if len(n) == 1:
        return mas1[int(n[0]) - 1]
    if len(n) == 2:
        if int(n[1]) == 0:
            return mas3[int(n[0]) - 2]
        return mas3[int(n[0]) - 2] + ' '+mas1[int(n[1]) - 1]


def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return lng_ru[number-1]
    if language == 'en':
        return lng_en[number-1]


def is_magic(date):
    n = list(map(int, date.split('.')))
    r1 = n[0] * n[1]
    r2 = int(str(n[2])[2:])
    if r1 == r2:
        return True
    return False


def is_pangram(text):
    r = set(text)
    if len(r) < 26:
        return False
    return True


if __name__ == '__main__':
    print(is_pangram(input()))
    # print(is_magic(input()))
    # print(get_month(input(), int(input())))
    # print(number_to_words(int(input())))
    # print(compute_binom(int(input()), int(input())))
    # print(get_shipping_cost(int(input())))
    # draw_triangle()
    pass
