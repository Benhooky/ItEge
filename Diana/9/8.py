f=open("ItEge/Diana/9/8.txt")
cnt=0
for x in f:
    lst=sorted([int(y) for y in x.split()])
    cnt4 = 0
    cnt1 = 0
    avgPovt = 0 
    for element in set(lst):
        if lst.count(element)==4:
            cnt4+=1
            avgPovt = element
        elif lst.count(element)==1:
            cnt1+=1
    if cnt4 == 1 and cnt1 == 3:
        if sum(lst)/len(lst)>avgPovt:
            cnt+=1
print(cnt)