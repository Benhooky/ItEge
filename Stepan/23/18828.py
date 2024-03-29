def f(from1, to1):
    if from1 > to1:
        return 0
    if from1 == to1:
        return 1
    else:
        return f(from1 + 1, to1) + f(from1 + 3, to1) + f(from1 * 3, to1)
print(f(4,10)*f(10,17)*f(17,23))