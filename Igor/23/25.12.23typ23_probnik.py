import math
from functools import lru_cache
@lru_cache
def f(x,y):
    if x < y or x == 4 or x == 43:
        return 0
    if x == y:
        return 1
    else:
        return f(x-1,y) + f(x//3,y) + f(int(math.sqrt(x)),y)
print(f(98,14) * f(14,2)) 