from functools import cache
import sys
sys.setrecursionlimit(10000)
@cache
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2*n-1) * f(n-1)
for i in range(1,3517):
    f(i)
print(f(3516)/f(3513))