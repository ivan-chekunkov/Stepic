def timur_and_his_team():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    result = z + (m - x - y) + n + k
    print(result)


def books_to_read():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    t = int(input())
    a = int(input())
    nm = n + m - x - t
    nk = n + k - z - t
    mk = m + k - y - t
    one_book = (n - nm - nk - t) + (m - nm - mk - t) + (k - nk - mk - t)
    two_book = nm + nk + mk
    null_book = a - one_book - two_book - t
    print(one_book)
    print(two_book)
    print(null_book)


def number_of_different_characters():
    print(len(set(input())))


def unique_figures():
    numbers = input()
    if len(numbers) == len(set(numbers)):
        print('YES')
    else:
        print('NO')


def all_10_digits():
    numbers_1 = input()
    numbers_2 = input()
    numbers_all = numbers_1 + numbers_2
    if len(set(numbers_all)) == 10:
        print('YES')
    else:
        print('NO')


def identical_sets():
    numbers_1 = set(input())
    numbers_2 = set(input())
    if numbers_1 == numbers_2:
        print('YES')
    else:
        print('NO')


def three_words():
    words = [set(i) for i in input().split()]
    if words[0] == words[1] == words[2]:
        print('YES')
    else:
        print('NO')


def unique_characters_1():
    print(*[len(set(input().lower())) for _ in range(int(input()))], sep='\n')


def unique_characters_2():
    result = ''
    for _ in range(int(input())):
        result += input()
    print(len(set(result.lower())))


def number_of_words_in_the_text():
    words = set(input().lower().split())
    result = set()
    for word in words:
        result.add(word.strip(".,;:-?!"))
    print(len(result))


def has_there_been_a_number_before():
    result = set()
    for num in input().split():
        num = int(num)
        if num in result:
            print('YES')
        else:
            print('NO')
            result.add(num)


def number_of_matching():
    nums_1 = set(input().split())
    nums_2 = set(input().split())
    result = nums_1 & nums_2
    print(len(result))


def common_numbers():
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    result = nums_1 & nums_2
    print(*sorted(result))


def the_numbers_of_the_first_row():
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    result = nums_1 - nums_2
    print(*sorted(result))


def general_figures():
    result = set()
    for num in range(int(input())):
        if num == 0:
            result = set(input())
        else:
            result &= set(input())
    print(*sorted(result))


def identical_numbers():
    nums_1 = set(input())
    nums_2 = set(input())
    if nums_1.isdisjoint(nums_2):
        print('NO')
    else:
        print('YES')


def all_numbers():
    nums_1 = set(input())
    nums_2 = set(input())
    if nums_2.issubset(nums_1):
        print('YES')
    else:
        print('NO')


def computer_science_lesson():
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    nums_3 = set(map(int, input().split()))
    result = sorted(nums_1 & nums_2 - nums_3, reverse=True)
    print(*result)


def math_lesson():
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    nums_3 = set(map(int, input().split()))
    result = sorted((nums_1 | nums_2 | nums_3) - (nums_1 & nums_2 & nums_3))
    print(*result)


def physics_lesson():
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    nums_3 = set(map(int, input().split()))
    result = sorted(nums_3 - nums_2 - nums_1, reverse=True)
    print(*result)


def biology_lesson():
    pattern = set(range(0, 11))
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    nums_3 = set(map(int, input().split()))
    result = sorted(pattern - nums_3 - nums_2 - nums_1)
    print(*result)


if __name__ == '__main__':
    biology_lesson()
    # physics_lesson()
    # math_lesson()
    # computer_science_lesson()
    # all_numbers()
    # identical_numbers()
    # general_figures()
    # the_numbers_of_the_first_row()
    # common_numbers()
    # number_of_matching()
    # has_there_been_a_number_before()
    # number_of_words_in_the_text()
    # unique_characters_2()
    # unique_characters_1()
    # three_words()
    # identical_sets()
    # all_10_digits()
    # unique_figures()
    # number_of_different_characters()
    # books_to_read()
    # timur_and_his_team()
    pass
