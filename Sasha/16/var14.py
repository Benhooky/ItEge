from functools import cache
@cache
def F(n):
    if n==1:
        return 1
    elif n%2==0:
        return n + 3 * F(n-1)
    else:
        return 2 + 2 * F(n-2)
for i in range(1,24):
    F(i)
print(F(23))
