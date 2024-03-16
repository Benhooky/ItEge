f= open('ItEge/Diana/17/17_11949 (1).txt')
lis=[int(x) for x in f]

res=[]
m68=0
for x in lis:
    if abs(x)%100==68:
        m68=max(m68,x)
for i in range(len(lis)-3):
    r=lis[i:i+4]
    c=0
    for s in r:
        if len(str(abs(s)))==2: c+=1
    if (c==1 or c==4) and sum(r)>=m68:
        res.append(sum(r))
print(len(res),max(res))