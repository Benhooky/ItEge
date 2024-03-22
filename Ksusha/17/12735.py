s=open('ItEge/Ksusha/17/17_12735.txt')
lis=[int(x) for x in s]
max09=0
con=0
minn=999999999999
for e in lis:
    if str(e)[-2:]=='09':
        max09=max(max09,e)
for i in range(0, len(lis)-2):
    cnt=0
    for a in range(0,3):
        if ((lis[i+a])%7)==0:
            cnt+=1
    if cnt==2:
        if (lis[i]+lis[i+1]+lis[i+2])<max09:
            con+=1
            minn=min(minn,lis[i]*lis[i+1]*lis[i+2])
print(con,minn)
