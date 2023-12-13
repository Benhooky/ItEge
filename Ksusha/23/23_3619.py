def f(from1, to):
    if from1>to:
        return 0
    elif from1==to:
        return 1
    else:
        return f(from1*3, to)  + f(from1+1,to)

print(f(4,34))