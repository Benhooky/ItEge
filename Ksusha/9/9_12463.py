f=open('ItEge/Ksusha/9/9_12463.txt')
lis=[list(map(int, x.split())) for x in f]
cnt=0
for i in lis:
    cntKv=0
    cnt2=0
    maxPair=0
    sumUniq=0
    i=sorted(i)
    for j in set(i):
        if i.count(j)==4:
            cntKv+=1
            maxPair=max(maxPair,j)
        elif i.count(j)==2:
            cnt2+=1
            maxPair=max(maxPair,j)
        elif i.count(j)==1:
            sumUniq+=j
    if cntKv==1 and cnt2==1 and len(set(i))==5 and sumUniq/3>=maxPair:
        cnt+=1
print(cnt)