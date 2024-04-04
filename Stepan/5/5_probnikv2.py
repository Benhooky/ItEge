def pr(s):
    k = ""
    while s > 0:
        k = str(s % 3) + k
        s //= 3
    return k
#вывести наибольший N для которого R меньше 100
Nmax = 0
for N in range(1, 100000):
    s = pr(N)
    if N % 7 == 0:
        s +=s[-2:]
    else:
        s += pr((N%7) * 3)
    R = int(s,3)
    if R < 100:
        Nmax = max(Nmax,N)
print(Nmax)