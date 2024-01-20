import sys
from functools import lru_cache


@lru_cache
def f(from1, to1):
    if from1 > to1 or from1 == 100:
        return 0
    if from1 == to1:
        return 1
    if from1 < to1:
        A = from1 + from1 % 10
        B = from1 + from1 % 68
        C = from1**2

        return (
            (f(A, to1) if A != from1 else 0)
            + (f(B, to1) if B != from1 else 0)
            + (f(C, to1) if C != from1 else 0)
        )


print(f(2, 68) * f(68, 680))
