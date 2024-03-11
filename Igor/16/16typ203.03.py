from functools import cache
@cache
def f(n):  
    if  n<3:
        return n
    if n > 2 and n%2!=0:
        return f(n-1)+f(n-2)+1
    if n > 2 and n%2==0:
        sum1 = 0
        for i in range(1,n):
            sum1 += f(i)
        return sum1
for i in range(39):
    f(i)
print(f(38))