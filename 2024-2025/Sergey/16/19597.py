from functools import cache  
@cache 
def F(n):
    if n<15:
        return 4
    if n>=15 and n%3==0:
        return F(2*n/3)+n-1
    if n>=15 and n%3!=0:
        return F(n-1)+3
for i in range(1,500):
    if F(i)==251:
        print(i)