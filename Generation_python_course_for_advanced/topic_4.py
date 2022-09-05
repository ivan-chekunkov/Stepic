def list_according_to_sample_1():
    number = int(input())
    matrix = []
    for _ in range(number):
        matrix.append([cell for cell in range(1, number + 1)])
    print(*matrix, sep='\n')


def list_according_to_sample_2():
    number = int(input())
    matrix = []
    for i in range(1, number + 1):
        matrix.append([cell for cell in range(1, i + 1)])
    print(*matrix, sep='\n')


def function_pascal_triangle(number_row_):
    result = []
    for index in range(number_row_ + 1):
        temp = []
        for j in range(index + 1):
            if j == 0 or j == index:
                temp.append(1)
            else:
                temp.append(result[index - 1][j - 1] + result[index - 1][j])
        result.append(temp)
    return result


def function_pascal_triangle_by_formula(number_row_):
    result = []
    from math import factorial
    for i in range(number_row_ + 1):
        result.append(int(factorial(number_row_) /
                          (factorial(i) * factorial(number_row_ - i))))
    return result


def pascal_triangle_1():
    number_row = int(input())
    print(function_pascal_triangle_by_formula(number_row))
    # print(function_pascal_triangle(number_row)[number_row])


def pascal_triangle_2():
    number_row = int(input())
    result_pascal_triangle = function_pascal_triangle(number_row - 1)
    for result_number_row in result_pascal_triangle:
        print(*result_number_row)


def packing_duplicates():
    text = list(input().split())
    text.append('*')
    result = []
    massive = [text[0]]
    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            massive.append(text[index])
        else:
            result.append(massive)
            massive = [text[index]]
    print(result)


def function_chunking(text, n):
    result = []
    massive = []
    for index, char in enumerate(text, start=1):
        if index == len(text):
            massive.append(char)
            result.append(massive)
            return result
        if index % n == 0:
            massive.append(char)
            result.append(massive)
            massive = []
        else:
            massive.append(char)


def chunking():
    text = list(input().split())
    n = int(input())
    print(function_chunking(text, n))


def sublists_of_the_list():
    main_list = list(input().split())
    result = [[]]
    slice_length = len(main_list) + 1
    for step in range(1, slice_length):
        for index in range(slice_length - step):
            result.append(main_list[index:index + step])
    print(result)


def output_matrix_1():
    row = int(input())
    column = int(input())
    matrix = []
    for _ in range(row):
        temp = []
        for _ in range(column):
            temp.append(input())
        matrix.append(temp)
    for number_row in range(row):
        print(*matrix[number_row])


def output_matrix_2():
    row = int(input())
    column = int(input())
    matrix = []
    for _ in range(row):
        temp = []
        for _ in range(column):
            temp.append(input())
        matrix.append(temp)
    for number_row in range(row):
        print(*matrix[number_row])
    print()
    for j in range(column):
        for i in range(row):
            print(matrix[i][j], end=' ')
        print()


def matrix_trace():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    sum_main_diagonal = 0
    for number_row in range(length_row):
        for number_column in range(length_row):
            if number_row == number_column:
                sum_main_diagonal += matrix[number_row][number_column]
    print(sum_main_diagonal)


def more_than_average():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    for row in matrix:
        average = sum(row) / len(row)
        count = 0
        for number in row:
            if number > average:
                count += 1
        print(count)


def maximum_in_area_1():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    maximum = matrix[0][0]
    for number_row in range(length_row):
        for number_column in range(length_row):
            if number_row >= number_column:
                if matrix[number_row][number_column] > maximum:
                    maximum = matrix[number_row][number_column]
    print(maximum)


def maximum_in_area_2():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    maximum = matrix[0][0]
    for number_row in range(length_row):
        for number_column in range(length_row):
            if ((number_row >= number_column and
                 number_row + number_column + 1 <= length_row)
                    or (number_row <= number_column and
                        number_row + number_column + 1 >= length_row)):
                if matrix[number_row][number_column] > maximum:
                    maximum = matrix[number_row][number_column]
    print(maximum)


def sums_of_quarters():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    sum_upper = 0
    sum_lower = 0
    sum_right = 0
    sum_left = 0
    for number_row in range(length_row):
        for number_column in range(length_row):
            if number_row < number_column:
                if number_row < length_row - number_column - 1:
                    sum_upper += matrix[number_row][number_column]
                if number_row > length_row - number_column - 1:
                    sum_right += matrix[number_row][number_column]
            if number_row > number_column:
                if number_row > length_row - number_column - 1:
                    sum_lower += matrix[number_row][number_column]
                if number_row < length_row - number_column - 1:
                    sum_left += matrix[number_row][number_column]
    print('Верхняя четверть:', sum_upper)
    print('Правая четверть:', sum_right)
    print('Нижняя четверть:', sum_lower)
    print('Левая четверть:', sum_left)


def multiplication_table():
    rows = int(input())
    columns = int(input())
    matrix = []
    for number_row in range(rows):
        temp = []
        for number_column in range(columns):
            temp.append(number_row * number_column)
        matrix.append(temp)
    for number_row in range(rows):
        for number_column in range(columns):
            print(str(matrix[number_row][number_column]).ljust(3), end=' ')
        print()


def maximum_in_the_table():
    rows = int(input())
    columns = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(rows)]
    maximum = matrix[0][0]
    cell_maximum = [0, 0]
    for number_row in range(rows):
        for number_column in range(columns):
            if matrix[number_row][number_column] > maximum:
                maximum = matrix[number_row][number_column]
                cell_maximum = [number_row, number_column]
    print(*cell_maximum)


def column_swapping():
    rows = int(input())
    columns = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(rows)]
    swap_1, swap_2 = [int(num) for num in input().split()]
    for number_row in range(rows):
        matrix[number_row][swap_1], matrix[number_row][swap_2] = \
            matrix[number_row][swap_2], matrix[number_row][swap_1]
    for row in matrix:
        print(*row)


def symmetric_matrix():
    length_row = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(length_row)]

    def symmetric():
        for i in range(length_row):
            for j in range(length_row):
                if matrix[i][j] != matrix[j][i]:
                    return 'NO'
        return 'YES'

    print(symmetric())


def exchange_of_diagonals():
    length_row = int(input())
    matrix = [input().split() for _ in range(length_row)]
    for i in range(length_row):
        matrix[i][i], matrix[length_row - i - 1][i] = \
            matrix[length_row - i - 1][i], matrix[i][i]
    for row in matrix:
        print(*row)


def mirroring():
    length_row = int(input())
    matrix = [input().split() for _ in range(length_row)]
    for number_row in range(length_row - 1, -1, -1):
        print(*matrix[number_row])


def matrix_rotation():
    length_row = int(input())
    matrix = [input().split() for _ in range(length_row)]
    new_matrix = [[0] * length_row for _ in range(length_row)]
    for number_row in range(length_row):
        for number_column in range(length_row):
            new_matrix[number_row][number_column] = \
                matrix[length_row - number_column - 1][number_row]
    for row in new_matrix:
        print(*row)


def knights_move():
    cell = input()
    coordinate_x = ord(cell[0]) - 97
    coordinate_y = 8 - int(cell[1])
    board = [['.'] * 8 for _ in range(8)]
    board[coordinate_y][coordinate_x] = 'N'
    for i in range(8):
        for j in range(8):
            if abs(coordinate_y - i) * abs(coordinate_x - j) == 2:
                board[i][j] = '*'
    for row in board:
        print(*row)


def magic_square():
    def srv_sum(matrix_, sum_srv):
        for row in matrix_:
            if sum(row) != sum_srv:
                return 'NO'
        return 'YES'

    def search(matrix_, num):
        if num == 0:
            return True
        count_num = 0
        for row in matrix_:
            count_num += row.count(num)
        if count_num > 1:
            return True
        return False

    length_row = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(length_row)]
    sum_main_diagonal = 0
    sum_secondary_diagonal = 0
    error = False
    for i in range(length_row):
        if error:
            break
        for j in range(length_row):
            if search(matrix, matrix[i][j]):
                error = True
                break
    if error:
        print('NO')
    else:
        for i in range(length_row):
            for j in range(length_row):
                if i == j:
                    sum_main_diagonal += matrix[i][j]
                if i == length_row - j - 1:
                    sum_secondary_diagonal += matrix[i][j]
        if sum_main_diagonal == sum_secondary_diagonal:
            print(srv_sum(matrix, sum_main_diagonal))
        else:
            print('NO')


def chess_board():
    rows, columns = [int(num) for num in input().split()]
    matrix = [['.'] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if (j + i) % 2 != 0:
                matrix[i][j] = '*'

    for row in matrix:
        print(*row)


def side_diagonal():
    length_row = int(input())
    matrix = [[0] * length_row for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            if i == length_row - 1 - j:
                matrix[i][j] = '1'
            elif i > length_row - 1 - j:
                matrix[i][j] = '2'
    for row in matrix:
        print(*row)


def filling_in_1():
    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    step = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = step
            step += 1
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_in_2():
    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = j * rows + i + 1
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_in_3():
    length_row = int(input())
    matrix = [[0] * length_row for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            if i == j or i == length_row - j - 1:
                matrix[i][j] = 1
    for i in range(length_row):
        for j in range(length_row):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_in_4():
    length_row = int(input())
    matrix = [[0] * length_row for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            if not (j < i < length_row - 1 - j or
                    j > i > length_row - 1 - j):
                matrix[i][j] = 1
    for i in range(length_row):
        for j in range(length_row):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_in_5():
    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = (j + i) % columns + 1
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]), end=' ')
        print()


def filling_with_a_snake():
    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                matrix[i][j] = i * columns + j + 1
            else:
                matrix[i][j] = (i + 1) * columns - j
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_with_diagonals():
    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    number = 1
    for k in range(rows + columns):
        for i in range(rows):
            for j in range(columns):
                if i + j == k:
                    matrix[i][j] = number
                    number += 1
    for i in range(rows):
        for j in range(columns):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def filling_with_a_spiral():
    def add_element(elem):
        elem += 1
        return elem, elem

    rows, columns = [int(num) for num in input().split()]
    matrix = [[0] * columns for _ in range(rows)]
    index_step = 0
    num_row = 0
    num_col = -1
    new_rows = rows
    new_columns = columns + 1
    while index_step < columns * rows:
        new_columns -= 1
        for _ in range(new_columns):
            num_col += 1
            index_step, matrix[num_row][num_col] = add_element(index_step)
        new_rows -= 1
        for _ in range(new_rows):
            num_row += 1
            index_step, matrix[num_row][num_col] = add_element(index_step)
        if index_step >= columns * rows:
            break
        new_columns -= 1
        for _ in range(new_columns):
            num_col -= 1
            index_step, matrix[num_row][num_col] = add_element(index_step)
        new_rows -= 1
        for _ in range(new_rows):
            num_row -= 1
            index_step, matrix[num_row][num_col] = add_element(index_step)
    for num_row in range(rows):
        for num_col in range(columns):
            print(str(matrix[num_row][num_col]).ljust(3), end=' ')
        print()


def matrix_addition():
    rows, columns = [int(num) for num in input().split()]
    matrix_one = [[int(num) for num in input().split()] for _ in range(rows)]
    input()
    matrix_two = [[int(num) for num in input().split()] for _ in range(rows)]
    matrix_three = matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_three[i][j] = matrix_one[i][j] + matrix_two[i][j]
    for i in range(rows):
        for j in range(columns):
            print(str(matrix_three[i][j]).ljust(3), end=' ')
        print()


def matrix_multiplication():
    rows_1, cols_1 = [int(num) for num in input().split()]
    matrix_one = [[int(num) for num in input().split()] for _ in range(rows_1)]
    input()
    rows_2, cols_2 = [int(num) for num in input().split()]
    matrix_two = [[int(num) for num in input().split()] for _ in range(rows_2)]
    matrix_three = [[0] * cols_2 for _ in range(rows_1)]
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                matrix_three[i][j] += matrix_one[i][k] * matrix_two[k][j]
    for i in range(rows_1):
        for j in range(cols_2):
            print(str(matrix_three[i][j]).ljust(3), end=' ')
        print()


def exponentiation_of_the_matrix():
    def multiplication(matrix_, matrix_copy_, length_row_):
        result_matrix = [[0] * length_row_ for _ in range(length_row_)]
        for i in range(length_row):
            for j in range(length_row):
                for k in range(length_row):
                    result_matrix[i][j] += matrix_copy[i][k] * matrix[k][j]
        return result_matrix

    length_row = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(length_row)]
    degree = int(input())
    matrix_copy = matrix.copy()
    for _ in range(degree - 1):
        matrix_copy = multiplication(matrix, matrix_copy, length_row)
    for row in range(length_row):
        for col in range(length_row):
            print(str(matrix_copy[row][col]).ljust(3), end=' ')
        print()


if __name__ == '__main__':
    # exponentiation_of_the_matrix()
    # matrix_multiplication()
    # matrix_addition()
    # filling_with_a_spiral()
    # filling_with_diagonals()
    # filling_with_a_snake()
    # filling_in_5()
    # filling_in_4()
    # filling_in_3()
    # filling_in_2()
    # filling_in_1()
    # side_diagonal()
    # chess_board()
    # magic_square()
    # knights_move()
    # matrix_rotation()
    # mirroring()
    # exchange_of_diagonals()
    # symmetric_matrix()
    # column_swapping()
    # maximum_in_the_table()
    # multiplication_table()
    # sums_of_quarters()
    # maximum_in_area_2()
    # maximum_in_area_1()
    # matrix_trace()
    # more_than_average()
    # output_matrix_2()
    # output_matrix_1()
    # sublists_of_the_list()
    # list_according_to_sample_1()
    # list_according_to_sample_2()
    # pascal_triangle_1()
    # pascal_triangle_2()
    # packing_duplicates()
    # chunking()
    pass
