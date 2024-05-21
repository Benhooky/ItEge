f = open('ItEge/Sasha/17/17_9786 (1).txt')
lis=[int(x) for x in f]
cnt=0
max25=-1000000000000000
lstAnswer = []
for x in lis:
    if abs(x)%100==25:
        max25=max(max25,x)
for i in range(len(lis)-2):
    troyka = [lis[i], lis[i+1],lis[i+2]]
    if len([x for x in troyka if 999<abs(x)<10000])<=2:
        if sum(troyka)<=max25:
            cnt+=1
            lstAnswer.append(sum(troyka))
print(cnt,max(lstAnswer))