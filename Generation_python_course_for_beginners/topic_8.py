def code_review_7():
    n = int(input())
    s = 0
    while n > 0:
        if n % 2 == 0:
            s += n % 10
        n //= 10
    print(s)


def code_review_8():
    n = 8
    count = 0
    maximum = -10**6 - 1
    for i in range(1, n + 1):
        x = int(input())
        if x % 4 == 0:
            count += 1
            if x > maximum:
                maximum = x
    if count > 0:
        print(count)
        print(maximum)
    else:
        print('NO')


def code_review_9():
    count = 0
    maximum = -1
    for i in range(4):
        x = int(input())
        if x % 2 != 0:
            count += 1
            if x > maximum:
                maximum = x
    if count > 0:
        print(count)
        print(maximum)
    else:
        print('NO')


def star_frame():
    n = int(input())
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print('*' * 19)
        else:
            print('*' + ' ' * 17 + '*')


def the_third_digit():
    n = int(input())
    while n > 999:
        n //= 10
    print(n % 10)


def all_together_2():
    n = int(input())
    count3 = 0
    countLast = 0
    countChet = 0
    sumBig5 = 0
    multyBig7 = 1
    count05 = 0
    last = n % 10
    while n > 0:
        x = n % 10
        if x == 3:
            count3 += 1
        if x == last:
            countLast += 1
        if x % 2 == 0:
            countChet += 1
        if x > 5:
            sumBig5 += x
        if x > 7:
            multyBig7 *= x
        if x == 0 or x == 5:
            count05 += 1
        n //= 10
    print(count3)
    print(countLast)
    print(countChet)
    print(sumBig5)
    print(multyBig7)
    print(count05)


if __name__ == '__main__':
    all_together_2()
    # the_third_digit()
    # star_frame()
    # code_review_9()
    # code_review_8()
    # code_review_7()
    pass
