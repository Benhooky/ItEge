f = [int(x) for x in open('ItEge/Pasha/17/17_11460.txt')]
max0 = 0
min0 = 100000000
cnt0 = 0
cnt1 = 0
for x in range(len(f)):
    if str(f[x])[0] == '8':
        max0 = max(max0, f[x])
for a in range(len(f) - 2):
    cnt0=0
    if (f[a] + f[a + 1] + f[a + 2]) >= max0:
        if str(abs(f[a]))[0] == '6':
            cnt0 += 1
        if str(abs(f[a + 1]))[0] == '6':
            cnt0 += 1
        if str(abs(f[a + 2]))[0] == '6':
            cnt0 += 1
        if cnt0 <= 1:
            cnt1 += 1
            min0 = min(min0, (f[a] + f[a + 1] + f[a + 2]))
print(cnt1, min0)