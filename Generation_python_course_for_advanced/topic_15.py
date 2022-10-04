import math
from functools import reduce


def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    matr = []
    for _ in range(n):
        temp = []
        for _ in range(m):
            temp.append(value)
        matr.append(temp)
    return matr


def mean(*args):
    summ = 0
    count = 0
    for i in args:
        if type(i) in (int, float):
            summ += i
            count += 1
    if count == 0:
        return 0
    return(summ / count)
