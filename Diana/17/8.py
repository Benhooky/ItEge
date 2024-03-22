f=open("ItEge/Diana/17/17 (7).txt")
lis=[int(x) for x in f]
res=[]
cnt=0
for i in range(len(lis)-1):
    for j in range(i+1,len(lis)):
        if abs(lis[j]-lis[i])%36==0:
            if j%13==0 or i%13==0:
                cnt+=1
                maxRaz=max(maxRaz,abs(lis[j]-lis[i]))
print(cnt,maxRaz)