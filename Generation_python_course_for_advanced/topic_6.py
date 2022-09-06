def the_top_of_the_parabola():
    a = int(input())
    b = int(input())
    c = int(input())
    summit = (-b / (2 * a), (4 * a * c - b ** 2) / (4 * a))
    print(summit)


def competitive_selection():
    result = []
    for i in range(int(input())):
        human = tuple(input().split())
        result.append(human)
    for i in result:
        print(*i)
    print()
    for i in result:
        if int(i[1]) > 3:
            print(*i)


def tribonacci_sequence():
    n = int(input())
    a0, a1, a2 = 1, 1, 1
    for i in range(n):
        print(a0, end=' ')
        a0, a1, a2 = a1, a2, a0 + a1 + a2


if __name__ == '__main__':
    tribonacci_sequence()
    # competitive_selection()
    # the_top_of_the_parabola()
    pass
