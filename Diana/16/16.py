from functools import cache
import sys
sys.setrecursionlimit(100000)
@cache
def F(n):
    if n>= 2024:
        return 1
    if n<2024:
        return F(n+2) + F(n+4)

res=[]
for x in range(3000,0,-1):
    res.append(F(x))
print(len(set(res)))