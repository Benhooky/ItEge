f = open("C:/progs/06.04/12098")

cnt=0
for x in f:
    lst=sorted([int(y) for y in x.split()])
    cnt3 = 0
    cnt1 = 0
    for el in set(lst):
        if lst.count(el)==3:
            if el%2==1:
                cnt3+=1
        elif lst.count(el)==1:
            if el%2==0:
                cnt1+=1
    if cnt3==1 and cnt1==1:
        cnt+=1
print(cnt)