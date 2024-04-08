
def f(from1, to1):
    if from1>to1 or from1 == 100:
        return 0
    if from1==to1:
        return 1
    #1
    return f(from1 + int(str(from1)[-1]),to1) + f(from1 + from1%68, to1) + f(from1**2,to1)
    #return f(from1 + from1%10)
print(f(2,64))

