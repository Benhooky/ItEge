from functools import cache
@cache
def F(n):
    if n<=3:
        return 1
    else:
        return (n+3)*F(n-2)
for i in range(1,2029):
    F(i)
print(F(2028)/F(2024))