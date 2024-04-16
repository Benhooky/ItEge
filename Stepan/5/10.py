maxr = 0
for x in range(1, 1000):
    s = bin(x)[2:]
    if x % 2 == 0:
        s += "00"
    else:
        s += "11"
    r = int(s, 2)
    if r < 134:
        maxr = max(r, maxr)
print(maxr)