f = [int(x) for x in open('ItEge/Stepan/17/17 (10).txt')]
s = 0
mx = 0
for i in range(len(f) - 1):
    for x in range(i + 1, len(f)):
        if (f[i] % 160 != f[x] % 160) and ((f[i] % 7 == 0) or (f[x] % 7 == 0)):
            s += 1
            mx = max(mx, f[i] + f[x])
print(s, mx)