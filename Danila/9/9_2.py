f = open('ItEge/Danila/9/9_2.txt')
for i in f:
    lis = sorted(int(x) for x in i.split())
    cnt1 = 0
    cnt2 = 0
    for j in set(lis):
        if lis.count(j) == 2:
            cnt2 += 1
        if lis.count(j) == 1:
            cnt1 += 1
    if cnt2 == 2 and cnt1 == 2:
        if lis[-1] != lis[-2]:
            if lis[0]*lis[-1] > sum(lis[1:-1]):
                print(sum(lis))
