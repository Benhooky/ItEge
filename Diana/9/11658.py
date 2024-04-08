f=open("C:/progs/06.04/11658")
cnt=0

for x in f:
    cnt+=1
    lst=[int(y) for y in x.split()]
    cnt3=0
    cnt1=0
    avrg=sum(lst)/len(lst)
    av=0
    for el in set(lst):
        if lst.count(el)==3:
            cnt3+=1
            av=el
        elif lst.count(el)==1:
            cnt1+=1
    if cnt1==4 and cnt3==1:
        if av>avrg:
            print(cnt)
print("Ответ 15958")