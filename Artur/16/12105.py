from functools import cache
@cache
def F(n):
    if n <= 5:
        return n
    if n > 5:
        return(2 * n - 8 + F(n - 2) + F(n - 1) // 8)
for i in range(1,164):
    F(i)
print(F(163))