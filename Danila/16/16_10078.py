from functools import lru_cache
@lru_cache
def F(n):
    if n < 3:
        return 2
    else:
        if n % 2 == 0:
            return 2 * F(n-2) - F(n-1) + 2
        else:
            return 2 * F(n-1) + F(n-2) - 2
print(F(170))