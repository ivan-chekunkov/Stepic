from typing import Counter
from itertools import combinations


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


def inversions(sequence: list[int]) -> int:
    result = 0
    for index_one in range(0, len(sequence)):
        for index_two in range(index_one + 1, len(sequence)):
            if sequence[index_one] > sequence[index_two]:
                result += 1
    return result


def inversions_2(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result


def pokemons():
    result = 0
    pokemons = Counter(line.rstrip() for line in sys.stdin.readlines())
    for count in pokemons.values():
        result += count - 1
    print(result)
