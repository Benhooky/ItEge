f=open("ItEge/2024-2025/Sergey/9/6602.txt")
cnt=0
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    cnt2=0
    cnt1=0
    sumPov=0
    avg=0
    for elem in set(lst):
        if lst.count(elem)==2:
            cnt2+=1
            sumPov+=elem*2
        if lst.count(elem)==1:
            cnt1+=1
            avg+=elem
    avg=avg/4
    first=cnt2==1 and cnt1==4
    second=avg>=sumPov
    if first and second:
        cnt+=1
print(cnt)