from functools import cache
from time import time
@cache
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return F(n / 2)
count = 0
start = time()
for n in range(0, 1000000000):
    if F(n) == 2:
        count += 1
print(time()-start)
print(count)
