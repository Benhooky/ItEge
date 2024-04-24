from functools import cache
@cache
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n*(n-1)+F(n-1)-F(n-2)
for i in range(2025):
    F(i)
print(F(2024)+F(2020)-F(2019))