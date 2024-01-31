from functools import lru_cache
@lru_cache
def F(n):
    if n == 0:
        return 0
    else:
        return F(n // 10) + (n % 10)
cnt = 0
for n in range(237567892, 1134567010):
    if F(n)>F(n+1):
        cnt+=1
print(cnt)