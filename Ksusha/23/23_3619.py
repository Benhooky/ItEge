def f(from1, to, cntAuse):
    if from1>to:
        return 0
    elif from1==to:
        return 1
    else:
        if cntAuse<3:
            return f(from1*3, to, cntAuse+1)  + f(from1+1,to, cntAuse)
        else:
            return f(from1+1,to, cntAuse)

print(f(4,34))