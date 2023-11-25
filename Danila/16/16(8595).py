import sys

sys.setrecursionlimit(10000)


def F(n):
    if n < 3:
        return 2
    if n > 2:
        return 2 * F(n - 2)


print(F(2222) / F(2182))
