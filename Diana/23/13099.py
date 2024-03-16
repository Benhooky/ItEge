def f(from1,to1,canIuseA):
    if from1>to1+1:
        return 0
    elif from1==to1:
        return 1
    else:
        if canIuseA:
            canIuseA = False
            return f(from1-1,to1,canIuseA)+f(from1*2,to1,True)+f(from1*3,to1,True)
        else:
            return f(from1*2,to1,True)+f(from1*3,to1,True)
print(f(3,15,True))