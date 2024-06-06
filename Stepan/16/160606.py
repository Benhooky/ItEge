from functools import cache
@cache
def f(n):
    if n > 3456:
        return n + 1
    if (n <= 3456) and (n % 3 == 0):
        return f(n + 1) + f(n + 2)
    if (n <= 3456) and (n % 3 != 0):
        return f(n + n % 3) + 2

for x in range(3456, 12, -1):
    f(x)

print(f(12)-f(17))
