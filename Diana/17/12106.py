f=open('ItEge/Diana/17/17_12106.txt')
lis=[int(x) for x in f]
res=[]

m117=10000
for x in lis:
    if x>0 and x%117==0:
        m117= min(m117,x)
for i in range(len(lis)-1):
    r=lis[i:i+2]
    c=0
    for s in r:
        if s<0: c+=1
    if (sum(r))%m117==0 and c==1:
        res.append((r[0])**2+(r[1])**2)
print(len(res),min(res))