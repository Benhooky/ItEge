from functools import cache
@cache
def F(n):
    if n<=3:
        return 2025
    if n>3:
        return 3*(n-1)*F(n-2)

for i in range(4965):
    F(i)
print (F(2027)/F(2023))