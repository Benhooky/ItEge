def f(x,y):
    if x < y:
        return 0
    if x == y:
        return 1
    else:
        return f(x-3,y) + f(x-1,y)
print(f(39,19)*f(19,16)*f(16,7))