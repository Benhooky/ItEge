a=open('ItEge/Ksusha/17/17 (1).txt')
cntpar=0
maxpar=0
lis=[int(x) for x in a]
for i in range (len(lis)-1):
    for j in range (i+1, len(lis)):
        if (lis[i]*lis[j])%14!=0:
            cntpar+=1
            maxpar=max(maxpar,lis[i]+lis[j])
print(cntpar,maxpar)

