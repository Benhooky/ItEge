#неверно
f=open('ItEge/Diana/27/27A_4685.txt')
n,m=[int(x) for x in f.readline().split()]
lst=[int(x) for x in f]
maxCont=0
sumi=sum(x//6+1 if x%6!=0 else x//6 for x in lst[0:2*m+1])
for i in range(m,n-3*m):
    sumj=sum(x//6+1 if x%6!=0 else x//6 for x in lst[2*m+1:4*m+2])
    for j in range(i+2*m+1,n-m-1):
        maxCont=max(sumi+sumj,maxCont)
        sumj= sumj - lst[j-m-1] + lst[j+m]
print(maxCont)
