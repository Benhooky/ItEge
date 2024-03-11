f = [int(x) for x in open('ItEge/Stepan/17/17_12471 (2).txt')]
max13 = 0
cnt = 0
sumAvg = 0
for i in f:
    if abs(i) % 100 == 13:
        max13 = max(max13, i)
for i in range(len(f)-2):
    r = [f[i],f[i+1],f[i+2]]
    if all(x%2==0 for x in r) or any(len(str(abs(x)))==2 for x in r):
        if sum(r) <= max13:
            cnt+=1
            sumAvg += sum(r)
print(cnt, sumAvg//cnt)
