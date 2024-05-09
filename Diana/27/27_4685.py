f=open('ItEge/Diana/27/27A_4685.txt')
n,m=[int(x) for x in f.readline().split()]
lst=[int(x) for x in f]
maxCont=0
for i in range(m,n-3*m):
    for j in range(i+2*m+1,n-m):
        sumi=sum(x//6+1 if x%6!=0 else x//6 for x in lst[i-m:i+m+1])
        sumj=sum(x//6+1 if x%6!=0 else x//6 for x in lst[j-m:j+m+1])
        maxCont=max(sumi+sumj,maxCont)
print(maxCont)