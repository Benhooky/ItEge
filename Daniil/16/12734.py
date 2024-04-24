from functools import cache
import sys
sys.setrecursionlimit(10000)
@cache
def F(n):
    if n<52:
        return n
    else:
        return 3*F(n-2)-n
print(F(15127)//F(15099))