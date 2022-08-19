import random as rd
import string


def creat_dict(is_dig: bool, is_up: bool, is_low: bool, is_char: bool) -> str:
    result = ''
    if is_dig:
        result += string.digits
    if is_up:
        result += string.ascii_uppercase
    if is_low:
        result += string.ascii_lowercase
    if is_char:
        result += '!#$%&*+-=?@^_'
    return result


def generate_password(length: int, chars: str) -> str:
    result = ''
    for _ in range(length):
        while True:
            char = rd.choice(chars)
            if len(result) == 0:
                result += char
                break
            if char != result[-1]:
                result += char
                break
    return result


def valid_int(text: str) -> tuple[int, bool]:
    try:
        num = int(text)
    except:
        return 0, False
    if 1 <= num <= 100:
        return num, True
    return 0, False


def valid_answear(text: str) -> bool:
    answear_true = ('yes', 'y', 'да', 'д', '1')
    if text.lower() in answear_true:
        return True
    return False


def request_conditions() -> tuple[int, int, bool, bool, bool, bool, bool]:
    print('Ответьте на вопросы уточняющие состав пароля!')
    while True:
        count_pas, status = valid_int(
            input('1) Количество паролей для генерации?  ')
        )
        if status:
            break
        print('Введите число от 1 до 100!')
    while True:
        len_pas, status = valid_int(input('2) Длину одного пароля?  '))
        if status:
            break
        print('Введите число от 1 до 100!')
    print('Отвечайте на вопросы - 1 = да, 0 = нет. По умолчанию НЕТ!')
    is_dig = valid_answear(input('3) Включать ли цифры 0123456789?  '))
    is_up = valid_answear(input(
        '4) Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?  ')
    )
    is_low = valid_answear(input(
        '5) Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?  ')
    )
    is_char = valid_answear(input('6) Включать ли символы !#$%&*+-=?@^_?  '))
    is_file = valid_answear(input('7) Скинуть пароли в файл?  '))
    return count_pas, len_pas, is_file, is_dig, is_up, is_low, is_char


def main():
    print('Вас приветствует программа генерации паролей!')
    count_pas, len_pas, is_file, *param_dict = request_conditions()
    chars = creat_dict(*param_dict)
    print('Вот ваши пароли:')
    print('=' * 15)
    passwords = []
    for _ in range(count_pas):
        password = generate_password(length=len_pas, chars=chars)
        passwords.append(password)
        print(password)
    if is_file:
        with open(file='password.txt', mode='w', encoding='utf-8') as file:
            for password in passwords:
                file.write(password + '\n')
    print('=' * 15)
    print('До скорых встреч!')


if __name__ == '__main__':
    main()
