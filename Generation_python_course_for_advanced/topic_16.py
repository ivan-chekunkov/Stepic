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
