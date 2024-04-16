def f1(x):
    return x-int(str(x**2)[0])
def f2(x):
    return x-sum([int(y) for y in str(x)])
def F(from1,to1):
    if to1>from1:
        return 0
    elif to1==from1:
        return 1
    else:
        return F(f1(from1),to1)+ F(f2(from1),to1)
print(F(32,1))