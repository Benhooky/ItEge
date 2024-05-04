from sys import setrecursionlimit
setrecursionlimit(10000)
def f(x,y):
    if x < y and  x == 21:
        return 0
    if x == y:
        return 1
    else:
        return f(x+2,y) + f(x+3,y) + f(x*5,y)
print(f(1,6) * f(6,35))