def traffic(n):
    if n > 0:
        print("Не парковаться")
        traffic(n - 1)


def func1(end, step=1):
    if step <= end:
        print(step)
        func1(end, step + 1)
