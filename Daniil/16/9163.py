from functools import cache
import sys
sys.setrecursionlimit(10000)
@cache
def F(n):
    if n>=2025:
        return 2025
    else:
        return F(n+1)-F(n+2)+7
for i in range(2030,14,-1):
    F(i)
print(F(15)-F(24))