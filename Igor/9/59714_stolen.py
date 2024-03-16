f = open('C:/Users/igort/Documents/launch/dz/9(10.03).txt')
cnt = 0
for s in f:
    a = sorted(list(map(int, s.split())))
    if len(set(a)) == 5:
        flag = 1
        sr1 = 0
        for i in range(0,len(a)):
            if a.count(a[i]) == 2:
                sr1 += a[i]
            if a.count(a[i]) > 2:
                flag = 0
                break
        if flag == 1:
            sr2 = (sum(a)-sr1)/3
            sr1 = sr1/4
            if sr2 > sr1:
                cnt += 1
print(cnt)