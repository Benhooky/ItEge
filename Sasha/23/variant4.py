def f(from1,to1):
    if from1>to1 or from1 == 21:
        return 0
    if from1 == to1:
        return 1
    return f(from1+2,to1)+f(from1+3,to1)+f(from1*5,to1)

print(f(1,6)*f(6,35))