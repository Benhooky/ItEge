from functools import cache
import sys
sys.setrecursionlimit(100000000)
@cache
def F(n):
    if n < 3:
        return 2**1024
    if n > 2:
        return 2*n + 3 + F(n-2)
for n in range(5000):
    F(n)
print(F(4048)-F(16))