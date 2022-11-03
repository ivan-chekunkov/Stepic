import random as rd
import os

mas = [
    ' -, |, |, |, |, |,---',
    ' ----|, |, |, |, |, |,---',
    ' ----|, |   |, |, |, |, |,---',
    ' ----|, |   |, |   O, |, |, |,---',
    ' ----|, |   |, |  _O, |, |, |,---',
    ' ----|, |   |, |  _O_, |, |, |,---',
    ' ----|, |   |, |  _O_, |   |, |, |,---',
    ' ----|, |   |, |  _O_, |   |, |  /, |,---',
    ' ----|, |   |, |  _O_, |   |, |  / \, |,---',
]

word_list = (
    'мамонт', 'кукла', 'заяц', 'книга', 'питон', 'студент',
    'кружка', 'справочник', 'функция', 'история', 'стол',
    'стул', 'железо',
)


def get_word():
    return rd.choice(word_list).upper()


def draw_gallows(mas):
    for i in mas.split(','):
        print(i)


def play():
    word = get_word()
    for t in range(10):
        answear = input('Каков твой ответ?  ').upper()
        os.system('cls')
        if answear == word:
            print('Ты выиграл!')
            break
        if t == 9:
            print('Ты проиграл!')
            print(f'Правильный ответ был - {word}')
            break
        draw_gallows(mas[t])
        print('=' * 10 + ' НЕВЕРНО ' + '=' * 10)


def main():
    print('Привет! Это игра виселица!')
    while True:
        answear = input('Будешь играть?  ')
        if answear.lower() in ('y', 'yes', 'д', 'да'):
            play()
        else:
            break
    print('Пока')


if __name__ == '__main__':
    main()
