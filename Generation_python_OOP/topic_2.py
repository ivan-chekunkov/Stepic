def darts():
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print(min(row, col, num - row + 1, num - col + 1), end=' ')
        print()
