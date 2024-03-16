f=open('ItEge/Diana/17/17_12249 (3).txt')
lis=[int(x) for x in f]
m=0
for x in lis:
    if len(str(abs(x)))==5 and abs(x)%10==3:
        m=max(m,x)
res=[]
for i in range(len(lis)-2):
    r=lis[i:i+3]
    if any(abs(r[x])%10==3 for x in range(3)) and sum(r)<=m:
        res.append(sum(r))
print(len(res),max(res))