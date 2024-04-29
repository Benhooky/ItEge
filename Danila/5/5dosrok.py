a=10000000000
for N in range(1, 10000):
    s=bin(N)[2:]
    if N % 2 == 0:
        s += '01'
    else:
        s = '1' + s + '1'
    R = int(s, 2)
    if R > 156:
        a = min(a, R)
print(a)