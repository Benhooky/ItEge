from functools import cache
import sys
sys.setrecursionlimit(100000)
@cache
def F(n):
    if n>=2025:
        return n
    else:
        return F(n+1)-F(n+2)+7
for i in range(3000,1,-1):
    F(i)
print(F(15)-F(24))