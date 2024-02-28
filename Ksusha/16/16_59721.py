import sys
from functools import lru_cache
sys.setrecursionlimit(100000000)
@lru_cache
def F(n):
    if n<=3:
        return n
    elif n>1:
        return n-1+F(n-1)+F(n-2)
print(F(2024)-F(2022))