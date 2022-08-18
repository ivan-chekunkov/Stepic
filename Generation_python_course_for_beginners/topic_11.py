def all_at_once_1():
    numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10,
               8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12,
               1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
    print(len(numbers))
    print(numbers[-1])
    print(numbers[::-1])
    if (5 in numbers) and (17 in numbers):
        print('YES')
    else:
        print('NO')
    del numbers[0]
    del numbers[-1]
    print(numbers)


def list_of_strings():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    print(s)


def alphabet():
    a = ord('a')
    s = []
    for i in range(1, 27):
        s.append(chr(a + i - 1) * i)
    print(s)


def list_of_cubes():
    n = int(input())
    s = []
    for i in range(n):
        s.append(int(input())**3)
    print(s)


def list_of_divisors():
    n = int(input())
    s = []
    for i in range(1, n + 1):
        if n % i == 0:
            s.append(i)
    print(s)


def sums_of_two():
    n = int(input())
    s = []
    b = []
    for i in range(1, n + 1):
        s.append(int(input()))
    for i in range(1, n):
        b.append(s[i] + s[i - 1])
    print(b)


def remove_odd_indexes():
    n = int(input())
    s = []
    b = []
    for _ in range(1, n + 1):
        s.append(int(input()))
    b = s[0::2]
    print(b)


def the_k_th_letter_of_the_word():
    n = int(input())
    s = []
    b = ''
    for i in range(n):
        s.append(input())
    k = int(input()) - 1
    for i in range(n):
        if len(s[i]) > k:
            b += s[i][k]
    print(b)


def characters_of_all_strings():
    n = int(input())
    s = []
    for _ in range(n):
        s.extend(input())
    print(s)


def function_value():
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(int(input()))
    for y in a:
        print(y)
    print()
    for y in a:
        print(y**2 + 2 * y + 1)


def remove_outliers():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    m1 = min(a)
    m2 = max(a)
    for y in a:
        if y == m1 or y == m2:
            continue
        print(y)


def no_duplicates():
    n = int(input())
    s = []
    for i in range(n):
        a = input()
        if a not in s:
            s.append(a)
    for i in range(len(s)):
        print(s[i])


def google_search_1():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    s = input()
    for i in range(len(a)):
        if s.upper() in a[i].upper():
            print(a[i])


def google_search_2():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    y = int(input())
    s = []
    for i in range(y):
        s.append(input())
    for i in range(len(a)):
        flag = True
        for j in range(len(s)):
            if s[j].upper() not in a[i].upper():
                flag = False
        if flag == True:
            print(a[i])


def negatives_zeros_and_positives():
    n = int(input())
    a = []
    b = []
    neg = []
    z = []
    pol = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        if a[i] < 0:
            neg.append(a[i])
        elif a[i] == 0:
            z.append(a[i])
        else:
            pol.append(a[i])
    b = neg + z + pol
    for i in range(len(b)):
        print(b[i])


def correct_ip_address():
    s = input()
    n = s.split('.')
    for i in n:
        if not 0 <= int(i) <= 255:
            print('НЕТ')
            break
    else:
        print('ДА')


def number_of_matching_pairs():
    k = input()
    s = 0
    r = k.split()
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            if r[i] == r[j]:
                s += 1
    print(s)


def all_at_once_2():
    numbers = [8, 9, 10, 11]
    numbers[1] = 17
    numbers.append(4)
    numbers.append(5)
    numbers.append(6)
    del numbers[0]
    numbers += numbers
    numbers.insert(3, 25)
    print(numbers)


def rearrange_min_and_max():
    m = input()
    names = m.split()
    for i in range(len(names)):
        names[i] = int(names[i])
    n1 = min(names)
    n2 = max(names)
    n1_i = names.index(n1)
    n2_i = names.index(n2)
    names[n1_i] = n2
    names[n2_i] = n1
    print(*names)


def number_of_articles():
    n = input()
    nn = n.lower().split()
    s = 0
    for i in nn:
        if i == 'a' or i == 'an' or i == 'the':
            s += 1
    print(f'Общее количество артиклей: {s}')


def hacking_the_brotherhood_of_steel():
    n = input()
    for _ in range(int(n[1:])):
        s = input()
        if '#' in s:
            s = s[:s.find('#')]
        print(s.rstrip())


def sorting_numbers():
    s = input()
    s1 = s.split()
    d = []
    for i in s1:
        d.append(int(i))
    d.sort()
    print(*d)
    d.sort(reverse=True)
    print(*d)


def palindromes():
    palindromes = [c for c in range(100, 1000) if str(c) == str(c)[::-1]]
    print(palindromes)


def list_expression_1():
    print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')


def list_expression_2():
    n = input()
    print(*[int(i)**3 for i in n.split()])


def in_one_line_1():
    n = input()
    print(*[i for i in n.split()], sep='\n')


def in_one_line_2():
    n = input()
    print(*[i for i in n if i.isdigit()], sep='')


def in_one_line_3():
    n = input().split()
    print(*[int(i)**2 for i in n if i[-1] in '046'], sep=' ')


def bubble_sort():
    a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96,
         -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6,
         52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91,
         44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44,
         -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75,
         -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39,
         38, -55, 7, -11, -26, -62, -84]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


def choice_sort():
    a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94,
         -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89,
         -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14,
         43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3,
         -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62,
         9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16,
         59, 59, 22, -24, -67, 76, -94, 59]
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    print(a)


if __name__ == '__main__':
    choice_sort()
    # bubble_sort()
    # in_one_line_3()
    # in_one_line_2()
    # in_one_line_1()
    # list_expression_2()
    # list_expression_1()
    # palindromes()
    # sorting_numbers()
    # hacking_the_brotherhood_of_steel()
    # number_of_articles()
    # rearrange_min_and_max()
    # all_at_once_2()
    # number_of_matching_pairs()
    # correct_ip_address()
    # negatives_zeros_and_positives()
    # google_search_2()
    # google_search_1()
    # no_duplicates()
    # remove_outliers()
    # function_value()
    # characters_of_all_strings()
    # the_k_th_letter_of_the_word()
    # remove_odd_indexes()
    # sums_of_two()
    # list_of_divisors()
    # list_of_cubes()
    # alphabet()
    # list_of_strings()
    # all_at_once_1()
    pass
