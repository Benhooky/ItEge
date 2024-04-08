f=open("C:/progs/06.04/11946")
cnt=0
for x in f:
    lst=[int(y) for y in x.split()]
    cnt3=0
    cnt1=0
    for el in set(lst):
        if lst.count(el)==3:
            cnt3+=1
        elif lst.count(el)==1:
            cnt1+=1
    if not((lst==sorted(lst))and(cnt3==1 and cnt1==4)):
        cnt+=1
print(cnt)
