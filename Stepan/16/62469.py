from functools import cache
cnt = 0
@cache
def F(n):
    if n <15:
        return n
    else:
        return F(n % 15) * F(n // 15) 
for n in range(3**15+1):
    if F(n) == 7560:
        cnt += 1
print(cnt) 