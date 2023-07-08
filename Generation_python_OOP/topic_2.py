def darts():
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print(min(row, col, num - row + 1, num - col + 1), end=' ')
        print()


def bracket_sequence():
    text = input()
    buffer = 0
    for char in text:
        if char == '(':
            buffer += 1
        elif char == ')' and buffer > 0:
            buffer -= 1
        else:
            return False
    return buffer == 0
