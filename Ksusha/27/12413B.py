s=open('ItEge/Ksusha/27/27A_12413.txt')
n=int(s.readline())
lis=[int(x) for x in s]
cnt=0
ans = {}
for i in range (len(lis)):
    if lis[i] not in ans.keys():
        ans[lis[i]] = 1
    else:
        ans[lis[i]] += 1
res = [x[1]*(x[1]-1) for x in ans.items()]
multy = 1
for i in res:
    if i!=0:
        multy*=i
print(multy)