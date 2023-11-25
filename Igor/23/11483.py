def f(from1, to):
    if from1 > to:
        return 0
    elif from1 == to:
        return 1
    else:
        return f(from1 + 1, to) + f(from1 + 3, to) + f(from1 * 3, to)

print(f(3,9)*f(9,27)*f(27,31))