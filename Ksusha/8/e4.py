from itertools import product
d=product('01234567',repeat=11)
d=[''.join(i) for i in d]
nechet=product('1357', repeat=2)

cnt=0
nechet=["".join(x) for x in nechet]
for i in d:
    cnt1=0
    for q in range (0,12):
        if int(i[q])%2==1:
            cnt1+=1
    if cnt1==3 and (all(s not in i for s in nechet)):
        cnt+=1
print(cnt)

