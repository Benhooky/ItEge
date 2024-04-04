def pr(s):
    k = ""
    while s > 0:
        k = str(s % 3) + k
        s //= 3
    return k

Rmin = 1000000000
for N in range(1, 100000):
    s = pr(N)
    if N % 7 == 0:
        s +=s[-2:]
    else:
        s += pr((N%7) * 3)
    R = int(s,3)
    if R > 369:
        Rmin = min(Rmin,R)
print(Rmin)