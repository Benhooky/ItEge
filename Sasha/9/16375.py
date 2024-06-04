f = open('ItEge/Sasha/9/9.txt')
cnt = 0
for line in f:
    lst = sorted([int(x) for x in line.split()])
    cnt2 = 0 #количество чисел повторяющихся дважды
    cnt1 = 0 #количество чисел повторяющихся один раз
    povt = 0
    minlist = []
    for x in set(lst):
        if lst.count(x)==2:
            cnt2+=1
            povt = x
        if lst.count(x)==1:
            cnt1+=1
            minlist.append(x)
    minlist.sort()
    usl1 = (cnt2 == 1 and cnt1 == 5)
    usl2 = minlist[0]*minlist[1]*minlist[2] > povt **2
    if usl1 and usl2:
        cnt+=1
print(cnt)