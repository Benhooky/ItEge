from functools import cache
import sys
sys.setrecursionlimit(10000)
@cache
def f(n):
    sumN=sum(int(x) for x in str(n))
    if n < 3:
        return 1
    if n > 2 and sumN%2==0:
        return f(n-1) - f(n-2)
    if n > 2 and sumN%2!=0:
        return f(n-1) + f(n//2)
print(f(100))