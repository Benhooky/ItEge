from functools import lru_cache
@lru_cache
def F(n):
    if n <= 5:
        return n
    if n > 5:
        return n*2 - 8 + F(n-2) + F(n-1)//8 
print(F(163))