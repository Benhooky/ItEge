from functools import cache

@cache
def F(n):
    if n<10:
        return n
    else:
        return F(n%10) + F(n//10)
    
cnt = 0
for n in range(2**20):
    if F(n) == 159:
        cnt+=1