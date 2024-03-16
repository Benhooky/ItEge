f=open('ItEge/Diana/17/17_11838.txt')
lis=[int(x) for x in f]
res=[]
m50=0
for x in lis:
    if abs(x)%100==50:
        m50=max(x, m50)

for i in range(len(lis)-2):
    r=lis[i:i+3]
    if all(len(str(abs(x)))==5 for x in r) and (r[0]!=r[1] or r[0]!=r[2] or r[1]!=r[2]):
        if sum(r)<=m50:
            res.append(sum(r))
print(len(res),max(res))