from functools import cache, lru_cache

@cache
def F(n):
    if n<=5:
        return n
    else:
        return 2*n-8+F(n-2)+F(n-1)//8
for i in range(170,0,-1):
    F(i)
print(F(163))