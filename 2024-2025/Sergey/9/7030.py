f=open("ItEge/2024-2025/Sergey/9/7030.txt")
cnt0=0
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    cnt1=0
    cnt2=0
    triangleLst = []
    for elem in set(lst):
        if lst.count(elem)==1:
            cnt1+=1
        if lst.count(elem)==2:
            cnt2+=1
            triangleLst.append(elem)
    first = cnt2 == 3 and cnt1 == 0
    triangleLst.sort()
    second = False
    if len(triangleLst) == 3: 
        second = triangleLst[0]**2+triangleLst[1]**2==triangleLst[2]**2
    if first and second:
        cnt0+=1
print(cnt0)