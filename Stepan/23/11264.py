def f(from1,to1):
    if from1>to1 or from1==32:
        return 0
    elif from1==to1:
        return 1
    else:
        return f(from1+2,to1) + f(from1+4,to1)
print(f(9,27)*f(27,29)*f(29,37))