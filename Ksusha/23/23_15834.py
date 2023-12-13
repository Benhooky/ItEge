def f(from1, to):
    if from1>to or from1==31:
        return 0
    elif from1==to:
        return 1
    else:
        return f(from1*2, to)  + f(from1+1,to)

print(f(2,15)*f(15,35))
