slov = {}
s = 5 * 3 ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991
while s > 0:
    ost = s % 17
    if ost not in slov:
        slov[ost] = 0
    else:
        slov[ost] += 1
    s //= 17
print(sorted(slov.items(), key=lambda x: x[1])[-1][0])
