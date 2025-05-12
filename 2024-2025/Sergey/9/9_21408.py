f=open("ItEge/2024-2025/Sergey/9/9_21408.txt")
cnt=0
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    cnt3=0
    cnt1=0
    maxPov=0
    nePov=0
    sumChet = 0
    for elem in set(lst):
        if lst.count(elem)==3:
            cnt3+=1
            maxPov=max(maxPov,elem)
        if lst.count(elem)==1:
            cnt1+=1
            nePov+=elem
    first= cnt3==2 and cnt1==1
    second=maxPov>nePov
    if first and second:
        cnt+=1
print(cnt)