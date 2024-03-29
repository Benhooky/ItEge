def f(from1, to1):
    if from1 > to1 or from1 == 24:
        return 0
    if from1 == to1:
        return 1
    else:
        return f(from1 + 1, to1) + f(from1 * 2 + 1, to1)
print(f(1,25))