f=open('ItEge/Ksusha/9/9_12918.txt')
lis=[list(map(int,x.split())) for x in f]
for i in lis:
    i=sorted(i)
    cntPairs=0
    for j in set(i):
        if i.count(j)==2:
            cntPairs+=1
    if len(set(i))==4 and i[-1]!=i[-2] and cntPairs==2 and (i[0]*i[-1]>sum(i[1:-1])):
        print(sum(i))
        break
