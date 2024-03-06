d=open('ItEge/Ksusha/17/17_11703 (1).txt')
lst=[int(i) for i in d]
max18=-1000000000
cnt_s=0
max_pr=-1000000000
for t in lst:
    if str(t)[-2:]=='18':
        max18=max(max18,t)
for x in range(0,(len(lst)-2)):
    cnt=0
    for j in range(0,3):
        if len(str(abs(lst[x+j])))==5:
            cnt+=1
    if cnt>0:
        if abs(lst[x]*lst[x+1]*lst[x+2])%max18==0:
            cnt_s+=1
            max_pr=max(max_pr,lst[x]*lst[x+1]*lst[x+2])
print(cnt_s,max_pr)

