S=open('ItEge/Ksusha/17/17_13088.txt')
lst=[int(i) for i in S]
cntcnt=0
maxmax=0
max_17=0
for t in range (len(lst)):
    if str(lst[t])[-2:]=='17':
        max_17=max(max_17, lst[t])
for x in range(0,len(lst)-2):
    cnt=0
    con=0
    for j in range(0,3):
        if len(str(lst[x+j]))==4:
            cnt+=1
        if lst[x+j]%5==0:
            con+=1
    if con>=1 and cnt==2:
        if lst[x]+lst[x+1]+lst[x+2]>max_17:
            cntcnt+=1
            maxmax=max(maxmax,lst[x]+lst[x+1]+lst[x+2])
print (cntcnt, maxmax)