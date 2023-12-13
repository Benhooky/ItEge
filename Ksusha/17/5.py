f=open('ItEge/Ksusha/17/17 (2).txt')
lis=[int (x) for x in f]
cntPar=0
min_par=1000000000000
minChislo=11111111111111
for i in range(len(lis)):
    if (99<(lis[i])<1000):
        if lis[i]%10==5:
            minChislo=min(minChislo,lis[i])

for x in range (len(lis)-1):
    stroka=sorted([lis[x],lis[x+1]])
    cnt=0
    for e in stroka:
        if 99<e<1000:
            cnt+=1
    if cnt==1:
        summPara=(stroka[0]+stroka[1])
        if summPara%minChislo==0:
            cntPar+=1
            min_par=min(min_par,(stroka[0]+stroka[1]) )
print(cntPar, min_par)



