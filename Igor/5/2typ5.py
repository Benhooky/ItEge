a = set()
for n in range(100, 3000):
    i = bin(n)[3:]
    razn = int(i, 2)
    pr = n - razn
    a.add(pr)
print(len(a))
