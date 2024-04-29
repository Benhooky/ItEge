def f(from1,to1):
    if from1 < to1:
        return 0
    if from1 == to1:
        return 1
    if from1>to1:
        return f(from1-1,to1)+f(from1-2,to1)+f(from1//4,to1)
print(f(26,20)*f(20,3))       