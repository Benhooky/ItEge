a = 100000000000000
for N in range(1, 10000):
    s = bin(N)[2:]
    if N % 3 == 0:
        s += s[-3:]
    else:
        s += bin((N % 3) * 3)[2:]
    R = int(s, 2)
    if R > 151:
        a = min(a, R)
print(a)
