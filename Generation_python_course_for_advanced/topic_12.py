import random
import string


def func_1():
    for _ in range(int(input())):
        if random.randint(0, 2) == 0:
            print('Орел')
        else:
            print('Решка')


def func_2():
    for _ in range(int(input())):
        i = random.randrange(1, 7)
        print(i)


def func_3():
    length = int(input())
    all_letters = list(range(97, 123)) + list(range(65, 91))
    length_all_letters = len(all_letters)
    for _ in range(length):
        index = random.randint(0, length_all_letters - 1)
        print(chr(all_letters[index]), end='')


def func_4():
    nums = []
    count = 0
    while count < 7:
        num = random.randint(1, 49)
        if num in nums:
            count -= 1
        else:
            nums.append(num)
        count += 1
    nums.sort()
    print(*nums)


def generate_ip():
    result = ''
    for _ in range(4):
        result += str(random.randint(0, 255)) + '.'
    return result[:-1]


def generate_index():
    result = ''
    chars = string.ascii_uppercase
    nums = string.digits
    for index in range(9):
        if index == 4:
            result += '_'
        elif index in [0, 1, 7, 8]:
            result += random.choice(chars)
        else:
            result += random.choice(nums)
    return result


def func_8():
    k = 0
    for i in range(10 ** 6):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
            k += 1
    print((k / 10 ** 6) * 16)


def func_9():
    k = 0
    for i in range(10 ** 6):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            k += 1
    s = (k * 4 / 10 ** 6) * 1
    print(s)


if __name__ == '__main__':
    func_9()
    # func_8()
    # password_generator_2()
    # password_generator_1()
    # secret_friend()
    # bingo()
    # func_7()
    # func_6()
    # print(func_5())
    # print(generate_index())
    # print(generate_ip())
    # func_4()
    # func_3()
    # func_2()
    # func_1()
    pass