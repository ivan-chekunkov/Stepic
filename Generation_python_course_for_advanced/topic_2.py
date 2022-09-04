def on_easy():
    one_number = int(input())
    two_number = int(input())
    print(
        one_number + two_number,
        one_number - two_number,
        one_number * two_number,
        one_number / two_number,
        one_number // two_number,
        one_number % two_number,
        (one_number ** 10 + two_number ** 10) ** 0.5,
        sep='\n'
    )


def body_mass_index():
    weight = float(input())
    height = float(input())

    if weight / height ** 2 < 18.5:
        print('Недостаточная масса')
    elif weight / height ** 2 > 25:
        print('Избыточная масса')
    else:
        print('Оптимальная масса')


def line_cost():
    row = input()
    length = len(row) * 60
    print(f'{length // 100} р. {length % 100} коп.')


def number_of_words():
    row = list(input().split())
    print(len(row))


def zodiac():
    animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух",
               "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
    year = int(input())
    while True:
        if year < 2000:
            year += 12
        elif year > 2011:
            year -= 12
        else:
            print(animals[year - 2000])
            break


def number_reversal():
    number = input()
    if len(number) == 6:
        revers_number = number[5:0:-1]
        revers_number = number[0] + revers_number
    else:
        revers_number = number[::-1]
    print(int(revers_number))


def standard_american_convention():
    number = input()
    revers_number = number[::-1]
    formatted_number = ''
    flag = 0
    for number in revers_number:
        if flag < 3:
            formatted_number += number
        else:
            formatted_number += ',' + number
            flag = 0
        flag += 1
    revers_number = formatted_number[::-1]
    print(revers_number)


def the_task_of_Josephus():
    quantity_of_people = int(input())
    length_step = int(input())
    circle_people = [i for i in range(1, quantity_of_people + 1)]
    step = 0
    while len(circle_people) > 1:
        step = (step + length_step - 1) % len(circle_people)
        circle_people.pop(step)
    return circle_people


def coordinate_quarters():
    quantity_of_points = int(input())
    amount_of_1_quarter = 0
    amount_of_2_quarter = 0
    amount_of_3_quarter = 0
    amount_of_4_quarter = 0
    for _ in range(quantity_of_points):
        array_of_points = list(map(int, input().split()))
        if array_of_points[0] > 0 and array_of_points[1] > 0:
            amount_of_1_quarter += 1
        elif array_of_points[0] > 0 and array_of_points[1] < 0:
            amount_of_4_quarter += 1
        elif array_of_points[0] < 0 and array_of_points[1] > 0:
            amount_of_2_quarter += 1
        elif array_of_points[0] < 0 and array_of_points[1] < 0:
            amount_of_3_quarter += 1
    print(f'Первая четверть: {amount_of_1_quarter}')
    print(f'Вторая четверть: {amount_of_2_quarter}')
    print(f'Третья четверть: {amount_of_3_quarter}')
    print(f'Четвертая четверть: {amount_of_4_quarter}')


def more_than_the_previous_one():
    array = list(map(int, input().split()))
    quantity_for_less = 0
    for index in range(1, len(array)):
        if array[index] - array[index - 1] > 0:
            quantity_for_less += 1
    print(quantity_for_less)


def back_forward_and_vice_versa():
    numbers_array = list(input().split())
    new_numbers_array = []
    for index in range(1, len(numbers_array), 2):
        new_numbers_array.append(numbers_array[index])
        new_numbers_array.append(numbers_array[index - 1])
    if len(numbers_array) % 2 != 0:
        new_numbers_array.append(numbers_array[-1])
    print(*new_numbers_array)


def a_shift_in_development():
    numbers_array = input().split()
    new_numbers_array = numbers_array[-1]
    for index in range(len(numbers_array) - 1):
        new_numbers_array += ' ' + numbers_array[index]
    print(new_numbers_array)


def various_elements():
    numbers_array = list(map(int, input().split()))
    quantity_of_different_numbers = 1
    compared = numbers_array[0]
    for number in numbers_array:
        if number != compared:
            compared = number
            quantity_of_different_numbers += 1
    print(quantity_of_different_numbers)


def the_product_of_numbers():
    quantity_of_numbers = int(input())
    numbers_array = [int(input()) for _ in range(quantity_of_numbers)]
    composition = int(input())
    if quantity_of_numbers == 1:
        print('НЕТ')
    else:
        for index in range(quantity_of_numbers):
            if composition % numbers_array[index] == 0:
                if (int(composition / numbers_array[index])
                        in numbers_array[index + 1:]):
                    print('ДА')
                    break
        else:
            print('НЕТ')


def rock_scissors_paper():
    gesture_one = input()
    gesture_two = input()
    if gesture_one == gesture_two:
        return 'ничья'
    if (gesture_one == 'камень' and gesture_two == 'ножницы' or
            gesture_one == 'ножницы' and gesture_two == 'бумага' or
            gesture_one == 'бумага' and gesture_two == 'камень'):
        return 'Тимур'
    return 'Руслан'


def rock_scissors_paper_lizard_spock():
    gesture_dictionary = {'камень': [1, 2, 4],
                          'ножницы': [2, 3, 4],
                          'бумага': [3, 1, 5],
                          'ящерица': [4, 3, 5],
                          'Спок': [5, 1, 2],
                          }
    gesture_one = gesture_dictionary[input()]
    gesture_two = gesture_dictionary[input()]
    if gesture_one[0] == gesture_two[0]:
        return 'ничья'
    if gesture_one[1] == gesture_two[0] or gesture_one[2] == gesture_two[0]:
        return 'Тимур'
    return 'Руслан'


def heads_and_tails():
    line = input()
    count_r = 0
    count_r_max = 0
    for char in line:
        if char == 'Р':
            count_r += 1
        else:
            if count_r > count_r_max:
                count_r_max = count_r
            count_r = 0
    if count_r > count_r_max:
        count_r_max = count_r
    return count_r_max


def silicon_valley():
    count_fridge = int(input())
    fridges = [input() for _ in range(count_fridge)]
    for count, fridge in enumerate(fridges):
        index = fridge.find('a')
        if index == -1 or index == len(fridge) - 1:
            continue
        else:
            index = fridge.find('n', index + 1)
            if index == -1 or index == len(fridge) - 1:
                continue
            else:
                index = fridge.find('t', index + 1)
                if index == -1 or index == len(fridge) - 1:
                    continue
                else:
                    index = fridge.find('o', index + 1)
                    if index == -1 or index == len(fridge) - 1:
                        continue
                    else:
                        index = fridge.find('n', index + 1)
                        if index == -1:
                            continue
                        else:
                            print(count + 1, end=' ')


def roskomnadzor_banned_the_letter_a():
    text = input() + ' запретил букву'
    dictionary = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л',
                  'м', 'н',
                  'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                  'ъ', 'ы',
                  'ь', 'э', 'ю', 'я']

    for letter in dictionary:
        text = text.lstrip(' ')
        text = text.rstrip(' ')
        text = text.replace('  ', ' ')
        if len(text) == 0:
            break
        if text.find(letter) == -1:
            continue
        print(text, letter)
        text = text.replace(letter, '')


if __name__ == '__main__':
    # roskomnadzor_banned_the_letter_a()
    # the_product_of_numbers()
    # various_elements()
    # a_shift_in_development()
    # back_forward_and_vice_versa()
    # more_than_the_previous_one()
    # coordinate_quarters()
    # standard_american_convention()
    # number_reversal()
    # on_easy()
    # body_mass_index()
    # line_cost()
    # number_of_words()
    # zodiac()
    # print(*the_task_of_Josephus())
    # print(rock_scissors_paper())
    # print(rock_scissors_paper_lizard_spock())
    # print(heads_and_tails
    # silicon_valley()
    pass
