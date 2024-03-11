f = open('ItEge/Danila/9/9364.txt')
cnt = 0
for i in f:
    lis = sorted(int(x) for x in i.split())
    sumChet = sum([x for x in lis if x%2==0])
    sumNeChet = sum([x for x in lis if x%2!=0])
    cnt1 = 0
    cnt2 = 0
    for j in set(lis):
        if lis.count(j) == 2:
            cnt2 += 1
        if lis.count(j) == 1:
            cnt1 += 1
    first = sumChet < sumNeChet
    second = cnt2 == 1 and cnt1 == 3
    if first ^ second:
        cnt += 1
print(cnt)
