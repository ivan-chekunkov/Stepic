def every_third():
    a = input()
    for i in range(3, len(a) + 3, 1):
        if i % 3 == 0:
            continue
        print(a[i - 3], sep='', end='')


def replace_me_completely():
    a = input()
    for i in range(len(a)):
        if a[i] == '1':
            print('one', sep='', end='')
        else:
            print(a[i], sep='', end='')


def delete_me_completely():
    a = input()
    for i in range(len(a)):
        if a[i] == '@':
            continue
        else:
            print(a[i], sep='', end='')


def second_occurrence():
    a = input()
    if a.count('f') == 0:
        print(-2)
    elif a.count('f') == 1:
        print(-1)
    else:
        b = a.find('f')
        print(a[b + 1:].find('f') + b + 1)


def upheaval():
    s = input()
    print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])


if __name__ == '__main__':
    upheaval()
    # second_occurrence()
    # delete_me_completely()
    # replace_me_completely()
    # every_third()
    pass
