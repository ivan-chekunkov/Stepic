def every_n_th_element():
    text = list(input().split())
    count_mas = int(input())
    new_mas = []
    for step_text in range(count_mas):
        temp = []
        for elem in range(step_text, len(text), count_mas):
            temp.append(text[elem])
        new_mas.append(temp)
    print(new_mas)


def maximum_matrix_2():
    length_row = int(input())
    matrix = []
    for _ in range(length_row):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    maximum = matrix[0][0]
    for i in range(length_row):
        for j in range(length_row):
            if i >= length_row - j - 1:
                if matrix[i][j] > maximum:
                    maximum = matrix[i][j]
    print(maximum)


def matrix_transposition():
    length_row = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            print(str(matrix[j][i]), end=' ')
        print()


def snowflake():
    length_row = int(input())
    matrix = [['.'] * length_row for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            if i == j or i == length_row - j - 1:
                matrix[j][i] = '*'
            elif i == length_row // 2 or j == length_row // 2:
                matrix[j][i] = '*'
    for row in matrix:
        print(*row)


def symmetric_matrix():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    result = 'YES'
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                result = 'NO'
                break
        if result == 'NO':
            break
    print(result)


def latin_square():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    pattern_row = [i for i in range(1, n + 1)]
    result = 'YES'
    for i in range(n):
        sum_col = []
        for j in range(n):
            sum_col.append(matrix[j][i])
        sum_col.sort()
        if sum_col != pattern_row:
            result = 'NO'
            break
    if result == 'YES':
        for row in matrix:
            row.sort()
            if row != pattern_row:
                result = 'NO'
                break
    print(result)


def queens_moves():
    cell = input()
    coordinate_x = ord(cell[0]) - 97
    coordinate_y = 8 - int(cell[1])
    board = [['.'] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if (i == coordinate_y or j == coordinate_x) or \
                    (abs(i - coordinate_y) == abs(j - coordinate_x)):
                board[i][j] = '*'
    board[coordinate_y][coordinate_x] = 'Q'
    for row in board:
        print(*row)


def diagonals_parallel_to_the_main():
    length_row = int(input())
    matrix = [[0] * length_row for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_row):
            matrix[i][j] = abs(i - j)
    for row in matrix:
        print(*row)


if __name__ == '__main__':
    # diagonals_parallel_to_the_main()
    # queens_moves()
    # latin_square()
    # symmetric_matrix()
    # snowflake()
    # matrix_transposition()
    # maximum_matrix_2()
    # every_n_th_element()
    pass
