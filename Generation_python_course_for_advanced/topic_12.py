import random
import string


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
