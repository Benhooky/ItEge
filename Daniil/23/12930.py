def f(from1,to1):
    if from1 == to1:
        return 1
    if from1>to1 or from1 == 11 or from1 == 12:
        return 0
    else:
        return f(from1+1,to1)+f(from1*2,to1)+f(from1**2,to1)
print(f(2,10)*f(10,40))