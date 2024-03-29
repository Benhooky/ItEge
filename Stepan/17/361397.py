f = [int(x) for x in open('ItEge/Stepan/17/17 (10).txt')]
cnt = 0
maxSum = -10000000
max17 = max(x for x in f if abs(x) % 100 == 17)
for i in range(len(f)-2):
    triple = [f[i], f[i+1], f[i+2]]
    cnt4 = sum(1 for x in triple if 999 < abs(x) < 10000)
    cntDel5 = sum(1 for x in triple if abs(x) % 5 == 0)
    if cnt4 == 2:
        if cntDel5 > 0:
            if sum(triple) > max17:
                cnt+=1
                maxSum = max(maxSum, sum(triple))
print(cnt,maxSum)