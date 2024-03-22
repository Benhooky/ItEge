f = [int(x) for x in open('ItEge/Stepan/17/17_10100 (2).txt')]
max13 = -100000000
cnt = 0
sumAvg = 0
maxSum = -10000000
for i in f:
    if abs(i) % 100 == 13:
        max13 = max(max13, i)

for i in range(len(f) - 2):
    r = [f[i], f[i + 1], f[i + 2]]
    cnt3 = 0
    for x in r:
        if len(str(abs(x))) == 3:
            cnt3+=1
    if sum(r) <= max13 and cnt3==2:
        cnt += 1
        maxSum = max(maxSum, sum(r))

print(cnt, maxSum)
