from string import digits
from itertools import product 
alph=(digits)[:8]
lst=[]
cnt=0
a=product(alph,repeat=7)
for i in a:
    if i[0]!="0":
        lst.append("".join(i))
lstBad = []
b = product('0246',repeat=2)
for i in b:
    lstBad.append("".join(i))
c = product('1357',repeat=2)
for i in c:
    lstBad.append("".join(i))
for x in lst:
    if x.count("0")==2:
        flag = True
        for badElem in lstBad:
            if badElem in x:
                flag=False
                break
        if flag:
            cnt+=1
print(cnt)