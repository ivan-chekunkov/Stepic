import calendar
import sys
import json


def func_1():
    blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},
                  {'Photos': 8, 'Comments': 1, 'Shares': 1},
                  {'Photos': 3, 'Likes': 19, 'Comments': 3}]
    total_likes = 0
    for post in blog_posts:
        try:
            total_likes += post['Likes']
        except:
            total_likes -= 1
    print(total_likes)


def func_2():
    food = ['chocolate', 'chicken', 'corn', 'sandwich',
            'soup', 'potatoes', 'beef', 'lox', 'lemonade']
    fifth = []
    for x in food:
        try:
            fifth.append(x[4])
        except:
            fifth.append('_')
    print(fifth)


def func_3():
    numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
    remainders = []
    for number in numbers:
        try:
            remainders.append(36 % number)
        except:
            pass
    print(remainders)


def only_numbers():
    lines = list(sys.stdin.readlines())
    sum_number = 0
    count_string = 0
    for line in lines:
        try:
            sum_number += int(line)
        except ValueError:
            try:
                sum_number += float(line)
            except:
                count_string += 1
    print(sum_number)
    print(count_string)


def january_february():
    months = dict(zip(range(1, 13), calendar.month_name[1:]))
    try:
        num = int(input())
        print(months[num])
    except KeyError:
        print('Введено число из недопустимого диапазона')
    except ValueError:
        print('Введено некорректное значение')


def add_to_list_in_dict(data: dict, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]


def readme_txt():
    name_file = input()
    try:
        with open(name_file, 'r') as file:
            text = file.read()
            print(text)
    except FileNotFoundError:
        print('​Файл не найден')


def get_weekday(number):
    week = {1: "Понедельник", 2: "Вторник", 3: "Среда",
            4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
    if type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    if number not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return week[number]


def get_id(names: list, name: str) -> int:
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1


def deserialization():
    name = input()
    try:
        with open(name) as json_file:
            try:
                text = json.load(json_file)
                print(text)
            except:
                print('Ошибка при десериализации')
    except:
        print('Файл не найден')
