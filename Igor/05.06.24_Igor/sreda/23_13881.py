from functools import cache
@cache
def f(x,y):
    if x == y:
        return 1
    if x > y or x == 20:
        return 0
    else:
        return f(x+1,y) + f(x+3,y) + f(x**2,y)
print(f(3,23)*f(23,25))