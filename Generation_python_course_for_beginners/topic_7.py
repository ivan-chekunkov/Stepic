import math


def population():
    m = int(input())
    p = int(input())
    n = int(input())
    for i in range(n):
        print(i+1, float(m))
        m = m+m*(p/100)


def sequence_of_numbers_1():
    m = int(input())
    n = int(input())
    for i in range(m, n):
        print(i)
    print(n)


def sequence_of_numbers_2():
    m = int(input())
    n = int(input())
    if m < n:
        for i in range(m, n + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            print(i)


def sequence_of_numbers_3():
    m = int(input())
    n = int(input())
    for i in range(m, n - 1, -1):
        if i % 2 != 0:
            print(i)


def sequence_of_numbers_4():
    m = int(input())
    n = int(input())
    for i in range(m, n + 1):
        if i % 17 == 0 or i % 15 == 0 or int(str(i)[-1]) == 9:
            print(i)


def multiplication_table():
    n = int(input())
    for i in range(1, 11):
        print(n, 'x', i, '=', n * i)


def number_of_numbers():
    m = int(input())
    n = int(input())
    count = 0
    for i in range(m, n + 1):
        if int(str(i**3)[-1]) == 4 or int(str(i**3)[-1]) == 9:
            count += 1
    print(count)


def sum_of_numbers():
    summa = 0
    n = int(input())
    for _ in range(n):
        summa += int(input())
    print(summa)


def asymptotic_approximation():
    n = int(input())
    summa = 0
    for i in range(1, n + 1):
        summa += 1 / i
    summa = summa - math.log(n)
    print(summa)


def sum_of_the_numbers_2():
    n = int(input())
    summa = 0
    for i in range(1, n + 1):
        if i**2 % 10 in [2, 5, 8]:
            summa += i
    print(summa)


def factorial():
    n = int(input())
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)


def without_zeros():
    p = 1
    for i in range(10):
        a = int(input())
        if a != 0:
            p = p * a
    print(p)


def sum_of_divisors():
    n = int(input())
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    print(s)


def alternating_amount_sign():
    n = int(input())
    if n == 1:
        s = 1
    elif n % 2 == 0:
        s = -1 * n // 2
    else:
        s = n-1 * n // 2
    print(s)


def the_largest_number():
    m1 = -1
    m2 = m1
    n = int(input())
    for _ in range(n):
        a = int(input())
        if a > m1:
            m2 = m1
            m1 = a
        elif a > m2:
            m2 = a
    print(m1)
    print(m2)


def only_even_numbers():
    flag = 0
    for i in range(10):
        n = int(input())
        if n % 2 == 0:
            flag += 1
    if flag == 10:
        print('YES')
    else:
        print('NO')


def the_fibonacci_sequence():
    n = int(input())
    f = ''
    pr = 0
    pr1 = 1
    for _ in range(n):
        pr1, pr = pr + pr1, pr1
        f = f + str(pr) + ' '
    print(f)


def pay_the_witcher_with_a_minted_coin():
    n = int(input())
    s = 0
    while n >= 25:
        s += n // 25
        n %= 25
    while n >= 10:
        s += n // 10
        n %= 10
    while n >= 5:
        s += n // 5
        n %= 5
    s += n
    print(s)


def reverse_order_1():
    num = int(input())
    while num != 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10


def reverse_order_2():
    num = int(input())
    s = ''
    while num != 0:
        last_digit = num % 10
        s += str(last_digit)
        num = num // 10
    print(s)


def max_and_min():
    num = int(input())
    small = 10
    big = -1
    while num != 0:
        last_digit = num % 10
        if last_digit > big:
            big = last_digit
        if last_digit < small:
            small = last_digit
        num = num // 10
    print('Максимальная цифра равна', big)
    print('Минимальная цифра равна', small)


def all_together():
    num = int(input())
    s = 0
    p = 1
    num2 = num
    while num != 0:
        last_digit = num % 10
        s += last_digit
        p *= last_digit
        num = num // 10
    print(s)
    print(len(str(num2)))
    print(p)
    print(s/len(str(num2)))
    print(last_digit)
    print(int(str(num2)[0]) + int(str(num2)[-1]))


def the_second_digit():
    num = int(input())
    a = 0
    b = 0
    while num != 0:
        last_digit = num % 10
        a = b
        b = last_digit
        num = num // 10
    print(a)


def identical_numbers():
    num = int(input())
    f = int(str(num)[0])
    has_seven = False
    while num != 0:
        last_digit = num % 10
        if last_digit != f:
            has_seven = True
        num = num // 10
    if has_seven == True:
        print('NO')
    else:
        print('YES')


def ordered_numbers():
    num = int(input())
    has_seven = False
    f = num % 10
    while num != 0:
        last_digit = num % 10
        if last_digit < f:
            has_seven = True
        f = last_digit
        num = num // 10
    if has_seven == True:
        print('NO')
    else:
        print('YES')


def smallest_divisor():
    n = int(input())
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            break


def follow_the_rules():
    n = int(input())
    i = 0
    while i < n:
        i += 1
        if 5 <= i <= 9:
            continue
        if 17 <= i <= 37:
            continue
        if 78 <= i <= 87:
            continue
        print(i)


def table_1():
    n = int(input())
    for _ in range(n):
        for _ in range(3):
            print(n, end=' ')
        print()


def table_2():
    n = int(input())
    for i in range(1, n + 1):
        for _ in range(5):
            print(i, end=' ')
        print()


def table_3():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, 9 + 1):
            print(i, '+', j, '=', i + j)
        print()


def the_star_triangle():
    n = int(input())
    r = n // 2
    flag = True
    j = 1
    while True:
        print(j * '*')
        if j <= r and flag == True:
            j += 1
        else:
            j -= 1
            flag = False
        if j == 0:
            break


def numerical_triangle_1():
    n = int(input())
    for i in range(1, n + 1):
        for _ in range(1, i + 1):
            print(i, end='')
        print()


def numerical_triangle_3():
    n = int(input())
    m = 1
    for i in range(1, n + 1):
        j = 0
        while True:
            if j < i:
                j += 1
                print(m, end=' ')
                m += 1
            else:
                print()
                break


def numerical_triangle_4():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, 2 * i):
            print(min(j, 2 * i - j), end='')
        print()


def divisors_1():
    a, b = int(input()), int(input())
    total_maximum = 0
    digit = 0

    for i in range(a, b + 1):
        maximum = 0
        for j in range(1, i + 1):
            if i % j == 0:
                maximum += j
            if maximum >= total_maximum:
                total_maximum = maximum
                digit = j
    print(digit, total_maximum)


def divisors_2():
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
        for y in range(1, i + 1):
            if i % y == 0:
                print('+', end='')
        print()


def digital_root():
    n = input()
    s = 0
    for i in n:
        s += int(i)
    d = 0
    for i in str(s):
        d += int(i)
    f = 0
    for i in str(d):
        f += int(i)
    print(f)


def sum_of_factorials():
    n = int(input())
    s = 0
    for i in range(1, n + 1):
        s += math.factorial(i)
    print(s)


def prime_numbers():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        if i == 1:
            continue
        f = True
        for y in range(2, i):
            if i % y == 0:
                f = False
        if f == True:
            print(i)


if __name__ == '__main__':
    prime_numbers()
    # sum_of_factorials()
    # digital_root()
    # divisors_2()
    # divisors_1()
    # numerical_triangle_4()
    # numerical_triangle_3()
    # numerical_triangle_1()
    # the_star_triangle()
    # table_3()
    # table_2()
    # table_1()
    # follow_the_rules()
    # smallest_divisor()
    # ordered_numbers()
    # identical_numbers()
    # the_second_digit()
    # all_together()
    # max_and_min()
    # reverse_order_2()
    # reverse_order_1()
    # pay_the_witcher_with_a_minted_coin()
    # the_fibonacci_sequence()
    # only_even_numbers()
    # the_largest_number()
    # alternating_amount_sign()
    # sum_of_divisors()
    # without_zeros()
    # factorial()
    # sum_of_the_numbers_2()
    # asymptotic_approximation()
    # sum_of_numbers()
    # number_of_numbers()
    # multiplication_table()
    # sequence_of_numbers_4()
    # sequence_of_numbers_3()
    # sequence_of_numbers_2()
    # sequence_of_numbers_1()
    # population()
    pass
