from functools import cache
@cache
def f(n):
    if n >= 7777:
        return n
    if n < 7777:
        return n + 5 + f(n + 5)

for i in range(7777, 1100, -1):
    f(i)

print(f(1101) - f(1111))