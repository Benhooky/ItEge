f=open("ItEge/2024-2025/Sergey/9/8467.txt")
cnt = 0
for line in f:
    lst =[int(x) for x in line.split()]
    lst.sort()
    cnt1=0
    for elem in set(lst):
        if lst.count(elem)==1:
            cnt1+=1
    first = cnt1 == 5
    second = (lst[-1]+lst[0])*2<lst[1]+lst[2]+lst[3]
    if first ^ second:
        cnt+=1
print(cnt)