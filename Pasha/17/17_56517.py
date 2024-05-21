f = [int(x) for x in open('ItEge/Pasha/17/17 (8).txt')]

mn = 10000000000000
cnt = 0
mx = -100000000000

for i in f:
    if abs(i) % 10 == 3:
        mn = min(mn, i)
        
for j in range(len(f) - 1):
    if abs(f[j]) % 10 == abs(f[j + 1]) % 10:
        if (abs(f[j]) % 3 == 0 and abs(f[j + 1]) % 3 != 0) or (abs(f[j]) % 3 != 0 and abs(f[j + 1]) % 3 == 0):
            if (f[j] ** 2 + f[j + 1] ** 2) < mn ** 2:
                cnt += 1
                mx = max(mx, f[j] ** 2 + f[j + 1] ** 2)
print(cnt, mx)