def traffic(n):
    if n > 0:
        print("Не парковаться")
        traffic(n - 1)


def func1(end, step=1):
    if step <= end:
        print(step)
        func1(end, step + 1)


def func2(step, nums):
    if step < len(nums):
        print(f"Элемент {step}: {nums[step]}")
        func2(step + 1, nums)


def triangle(h):
    if h > 0:
        print("*" * h)
        triangle(h - 1)
