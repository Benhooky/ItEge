from functools import cache
@cache
def f(n, k):
    if k == 0:
        return 0
    if (k > 0) and ((n % k) == 0):
        return f(n, k - 1) + k ** 2
    if (k > 0) and ((n % k) != 0):
        return f(n, k - 1)
for k in range(123456789+1):
    f(11223456789, k)
print(f(11223456789,123456789))