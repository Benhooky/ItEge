from itertools import product

s = product('АЗИМНОПРТ', repeat=5)
lst=["".join(x) for x in s]
cnt=0
for i in lst:
    cnt+=1
    if i[0]=='Н' and i.count('Р')==2:
        if cnt%2==0:
            print(cnt,i)