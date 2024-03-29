from functools import cache
@cache
def F(n):
    if n<=5:
        return n
    else:
        return 2*n-8+F(n-1)//8+F(n-2)
for i in range(20001):
    F(i)
print(F(20000))