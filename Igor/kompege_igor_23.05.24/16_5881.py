from functools import cache
@cache
def f(n):
    if n < 10:
        return 0
    if n >= 10:
        return f(n//10) + (n//10%10) - (n%10)
for i in range(10**10 + 1):
    f(i)
pass