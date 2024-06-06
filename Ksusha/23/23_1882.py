def f(from1, to, canUseA):
    if from1>to:
        return 0
    elif from1==to:
        return 1
    else:
        if canUseA:
            return f(from1*3, to, False)  + f(from1+3,to, True) + f(from1+1,to, True)
        else:
            return  f(from1+3,to, True) + f(from1+1,to, True)

print(f(4,10,True)*f(10,17,True)*f(17,23,True))