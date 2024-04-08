f=open("C:/progs/06.04/11830")
cnt=0
for x in f:
    lst=[int(y) for y in x.split()]
    cnt1=0
    cnt2=0
    pr1=1
    pr2=1
    for el in set(lst):
        if lst.count(el)==2:
            cnt2+=1
            pr2*=el**2
        elif lst.count(el)==1:
            cnt1+=1
            pr1*=el
    if cnt2==2 and cnt1==3:
        if pr2>2*pr1:
            cnt+=1
print(cnt)

