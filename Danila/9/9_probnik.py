f = open('ItEge/Danila/9/9_1.txt')
number = 0
result = 0
for i in f:
    number +=1
    lis = sorted(int(x) for x in i.split())
    cnt1 = 0
    cnt3 = 0
    avgPovt = 0
    for j in set(lis):
        if lis.count(j)==3:
            cnt3+=1
            avgPovt += j
        elif lis.count(j)==1:
            cnt1+=1
    if cnt1==4 and cnt3==1:
        if sum(lis)/7<avgPovt:
            result = number
print(result)