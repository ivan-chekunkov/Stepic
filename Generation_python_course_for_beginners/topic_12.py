def list_of_even_numbers():
    n = int(input())
    print([i for i in range(2, n + 1, 2)])


def sum_of_two_lists():
    n = input().split()
    m = input().split()
    s = []
    for i in range(len(n)):
        s.append(int(n[i]) + int(m[i]))
    print(*s, sep=' ')


def sum_of_numbers():
    n = input().split()
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    print(*n, sep='+', end='')
    print(f'={s}')


def valid_number():
    n = input().split('-')
    flag = False
    if len(n) == 4:
        if (len(n[0]) == 1 and len(n[1]) == 3 and
                len(n[2]) == 3 and len(n[3]) == 4):
            if (int(n[0]) == 7 and n[1].isdigit() and
                    n[2].isdigit() and n[3].isdigit()):
                flag = True
    if len(n) == 3:
        if len(n[0]) == 3 and len(n[1]) == 3 and len(n[2]) == 4:
            if n[0].isdigit() and n[1].isdigit() and n[2].isdigit():
                flag = True
    if flag == True:
        print('YES')
    else:
        print('NO')


def the_longest():
    print(max([len(i) for i in input().split()]))


def youth_jargon():
    n = input().split()
    print(*[i[1:] + i[0] + 'ки' for i in n])


if __name__ == '__main__':
    youth_jargon()
    # the_longest()
    # valid_number()
    # sum_of_numbers()
    # sum_of_two_lists()
    # list_of_even_numbers()
    pass
