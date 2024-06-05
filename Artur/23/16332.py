def f(from1, to1):
    if from1 > to1:
        return 0
    elif from1 == to1:
        return 1
    else:
        return f(from1 + 1,to1) + f(from1+2,to1) + f(from1*2, to1)
print(f(4,11) * f(11,13) * f(13,15))
