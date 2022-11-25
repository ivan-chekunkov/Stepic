from functools import reduce


def generate_letter(
    mail, name, date, time, place, teacher='Тимур Гуев', number=17
):
    result = ''
    result += f'To: {mail}\n'
    result += f'Приветствую, {name}!\n'
    result += f'Вам назначен экзамен, который пройдет {date}, в {time}.\n'
    result += f'По адресу: {place}.\n'
    result += f'Экзамен будет проводить {teacher} в кабинете {number}.\n'
    result += 'Желаем удачи на экзамене!'
    return result


def pretty_print(data, side='-', delimiter='|'):
    line = f" {delimiter} ".join(map(str, data))
    print(' ' + side * (2 + len(line)))
    print(delimiter + ' ' + line + ' ' + delimiter)
    print(' ' + side * (2 + len(line)))


def concat(*args, sep=' '):
    return reduce(lambda x, y: str(x) + sep + str(y), args)


def product_of_odds(data):
    return reduce(lambda x, y: x * y if y % 2 == 1 else x, data, 1)


def gepatr():
    result = {}
    for _ in range(int(input())):
        word = input()
        gep = reduce(lambda x, y: x + ord(y), word.upper(), 0) - len(word) * 65
        result[word] = int(gep)
    res = sorted(result)
    otv = sorted(res, key=lambda x: result.get(x))
    print(*otv, sep='\n')


def sort_ip():
    result = {}
    for _ in range(int(input())):
        ip = input()
        ip_nums = tuple(map(int, ip.split('.')))
        gep = ip_nums[0] * 256 ** 3 + ip_nums[1] * \
            256 ** 2 + ip_nums[2] * 256 + ip_nums[3]
        result[ip] = gep
    res = sorted(result, key=lambda x: result.get(x))
    print(*res, sep='\n')


if __name__ == '__main__':
    sort_ip()
    # gepatr()
    # print(concat('hello', 'python', 'and', 'stepik', sep='*'))
    # pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
    # print(generate_letter('lara@yandex.ru', 'Лариса',
    #       '10 декабря', '12:00', 'Часова 23, корпус 2'))
    pass
