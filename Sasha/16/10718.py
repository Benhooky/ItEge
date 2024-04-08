from functools import cache
@cache
def F(n):
    if n<3:
        return 2
    elif n%2==0:
        return 2 * F(n-2) - F(n-1) + 2
    else:
        return 2 * F(n-1) + F(n-2) - 2
for i in range(171):
    F(i)
print(F(170))