from functools import cache
@cache
def F(n):
    if n<=3:
        return n-1
    if n>3 and n%2==0:
        return F(n-2)+n/2-F(n-4)
    if n>3 and n%2==1:
        return F(n-1)*n + F(n-2)
    
for i in range(4965):
    F(i)
    
print(F(4952)+2*F(4958)+F(4964))