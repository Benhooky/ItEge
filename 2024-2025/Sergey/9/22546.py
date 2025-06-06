f=open("ItEge/2024-2025/Sergey/9/22546.txt")
cnt=0 
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    cnt1=0
    for elem in set(lst):
        if lst.count(elem)==1:
            cnt1+=1
    if lst[0]*lst[1]<=sum(lst[2:]):
        if cnt1==7:
            cnt+=1
print(cnt)