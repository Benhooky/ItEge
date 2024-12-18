f=open("ItEge/2024-2025/Sergey/9/16375.txt")
cnt=0
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    cnt2=0
    cnt1=0
    lstNePovt=[]
    Pov=0
    for elem in set(lst):
        if lst.count(elem)==1:
            cnt1+=1
            lstNePovt.append(elem)
        if lst.count(elem)==2:
            cnt2+=1
            Pov=elem
    lstNePovt.sort()
    first = cnt2==1 and cnt1==5
    if len(lstNePovt)==5:
        second = lstNePovt[0]*lstNePovt[1]*lstNePovt[2]>Pov**2
        if first and second:
            cnt+=1
print(cnt)
