f=open("ItEge/Diana/9/12918.txt")
for x in f:
    lst=sorted([int(y) for y in x.split()])
    cnt2=0
    cnt1=0
    for k in set(lst):
        if lst.count(k)==2:
            cnt2+=1
        elif lst.count(k)==1:
            cnt1+=1
    if cnt2==2 and cnt1==2:
        if lst[-1]!=lst[-2]:
            if lst[0]*lst[-1]>sum(lst[1:-1]):
                print(sum(lst))
                break