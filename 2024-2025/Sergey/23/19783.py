def f(from1,to1):
    if from1==to1:
        return 1
    elif from1<to1 or from1==18:
        return 0
    else:
        return f(from1-2,to1)+f(from1/2 if from1%2==0 else from1-3, to1)
print(f(55,3))