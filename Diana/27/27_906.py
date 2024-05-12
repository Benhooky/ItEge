f=open('ItEge/Diana/27/27-A_906.txt')
N=int(f.readline())
lst = []
for i in f:
    j = [int(x) for x in i.split()]
    lst.append([j[0],j[1],abs(j[1]-j[0]),abs(j[1]-j[0])%10])
lst = sorted(lst,key=lambda x: x[2])
summax=0
res=[]
for i in range(N):
    summax+=max(lst[i])
ost = summax%10
for x in lst:
    print(x)
for i in range(N):
    for j in range(N):
        if summax%10==8:
            res.append(summax)
        elif (summax-max(lst[j])+min(lst[j]))%10==8:
            res.append(summax-max(lst[j])+min(lst[j]))
        else:summax=summax-max(lst[j])+min(lst[j])
print(max(res))