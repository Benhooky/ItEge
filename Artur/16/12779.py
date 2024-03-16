import sys
sys.setrecursionlimit(5000)
def F(n,x):
    if n>=3000:
        return n
    else:
        return n+x+F(n+2,x)
for x in range(-5000,5000):
    if F(2984,x)-F(2988,x)==5916:
        print(x)
        break