f=open('ItEge/Diana/9/90506.txt')
cnt=0
summ=0
for x in f:
    lst=[int(y) for y in x.split()]
    s=set(lst)
    cnt2=0
    cnt1=0
    for i in s:
        if lst.count(i) ==2:
            cnt2+=1
        elif lst.count(i)==1:
            cnt1+=1
    if cnt2==2 and cnt1==4:
        if lst.count(min(lst))==1:
            summ+=sum(lst)
            cnt+=8
print(summ/cnt)