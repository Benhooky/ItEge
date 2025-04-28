f=open("ItEge/2024-2025/Sergey/9/18364.txt")
cnt=0
for line in f:
    lst=[int(x) for x in line.split()]
    lst.sort()
    countPovt=0
    sumNePov=0
    mulPov=1
    for elem in set(lst):
        if lst.count(elem)>=2:
            countPovt+=1
            mulPov=mulPov*elem**lst.count(elem)
        else:
            sumNePov+=elem
    first=countPovt>0
    second=sumNePov*3<=mulPov
    if first and second:
        cnt+=1
print(cnt)