f=open('ItEge/Diana/17/17 (14).txt')
lis=[int(x) for x in f]
res=[]
for i in range(1,len(lis)):
    if abs(lis[i-1])>abs(lis[i]):
        if abs(lis[i] + lis[i - 1]) % 27 == 0:
            res.append((lis[i]+lis[i-1]))
print(len(res),abs(min(res)))