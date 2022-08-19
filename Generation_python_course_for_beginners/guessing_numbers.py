import random as rd

DICT_ANSWEAR = (
    'Добро пожаловать в числовую угадайку',
    'Слишком много, попробуйте еще раз',
    'Слишком мало, попробуйте еще раз',
    'Вы угадали, поздравляем!',
    'А может быть все-таки введем целое число от 1 до 100?',
    'Спасибо, что играли в числовую угадайку. Еще увидимся...',
)


def is_valid(text):
    try:
        if 1 <= int(text) <= 100:
            return True
        return False
    except:
        return False


def result_answear(num, pattern):
    if num == pattern:
        return DICT_ANSWEAR[3], 1
    if num > pattern:
        return DICT_ANSWEAR[1], 0
    return DICT_ANSWEAR[2], 0


def genedate_number():
    return rd.randint(1, 100)


def main():
    print(DICT_ANSWEAR[0])
    answear = genedate_number()
    while True:
        input_num = input()
        if is_valid(input_num):
            num = int(input_num)
            text_answear, status = result_answear(num, answear)
            print(text_answear)
            if status == 1:
                break
        else:
            print(DICT_ANSWEAR[4])


if __name__ == '__main__':
    main()
