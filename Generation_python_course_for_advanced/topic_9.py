def homework():
    n = int(input())
    m = int(input())
    k = int(input())
    p = int(input())
    print(n - (m + k - p))


def voskhod_satellite():
    indicators = input().split()
    unique_indicators = set(indicators)
    print(len(indicators) - len(unique_indicators))


def cities():
    cityes = set(input() for _ in range(int(input())))
    if input() in cityes:
        print('REPEAT')
    else:
        print('OK')


def books_to_read():
    books_in_bibl = int(input())
    books_to_read = int(input())
    books = set(input() for _ in range(books_in_bibl))
    for _ in range(books_to_read):
        if input() in books:
            print('YES')
            continue
        print('NO')


def a_strange_hobby():
    one_task = set(int(i) for i in input().split())
    two_task = set(int(i) for i in input().split())
    intersection_task = sorted(one_task.intersection(two_task), reverse=True)
    if len(intersection_task) == 0:
        print('BAD DAY')
    else:
        print(*intersection_task)


def beegeek_1_online_school():
    pattern = set(int(i) for i in input().split())
    answer = set(int(i) for i in input().split())
    if pattern == answer:
        print('YES')
    else:
        print('NO')


def beegeek_2_online_school():
    m = int(input())
    n = int(input())
    mathematics = set(input() for _ in range(m))
    informatics = set(input() for _ in range(n))
    print(len(mathematics) - len(mathematics & informatics))


def beegeek_3_online_school():
    m = int(input())
    n = int(input())
    mathematics = set(input() for _ in range(m))
    informatics = set(input() for _ in range(n))
    count = mathematics.symmetric_difference(informatics)
    if len(count) == 0:
        print('NO')
    else:
        print(len(count))


def beegeek_4_online_school():
    one_teacher = set(input().split())
    two_teacher = set(input().split())
    students = sorted(one_teacher.union(two_teacher))
    print(*students)


def beegeek_5_online_school():
    m = int(input())
    n = int(input())
    one_discipline = set()
    two_discipline = set()
    i = 0
    while i < n + m:
        student = input()
        if student in one_discipline:
            two_discipline.add(student)
            i += 1
            continue
        one_discipline.add(student)
        i += 1
    count = one_discipline - two_discipline
    if len(count) == 0:
        print('NO')
    else:
        print(len(count))


def beegeek_6_online_school():
    all_lesson = set()
    for i in range(int(input())):
        one_lesson = set()
        for _ in range(int(input())):
            one_lesson.add(input())
        if i == 0:
            all_lesson = one_lesson.copy()
        else:
            all_lesson.intersection_update(one_lesson)
    students = sorted(all_lesson)
    print(*students, sep='\n')


if __name__ == '__main__':
    beegeek_6_online_school()
    # beegeek_5_online_school()
    # beegeek_4_online_school()
    # beegeek_3_online_school()
    # beegeek_2_online_school()
    # beegeek_1_online_school()
    # a_strange_hobby()
    # books_to_read()
    # cities()
    # voskhod_satellite()
    # homework()
    pass
