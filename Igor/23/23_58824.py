def f(fromm, to):
    if fromm == to:
        return 1
    if fromm < to or fromm == 5:
        return 0
    if fromm > to:
        return f(fromm - 1, to) + f(fromm // 2, to)


print(f(45, 15) * f(15, 3))
