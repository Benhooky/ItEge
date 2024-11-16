from itertools import product
from string import ascii_uppercase,digits
alph =  (digits + ascii_uppercase)[:15]
f = product(alph,repeat = 5)
cnt = 0
lst = []
for x in f:
    lst.append(''.join(x))
for x in lst:
    if x.count('8') == 1 and x[0]!='0':
        cnt9 = 0
        for num in x:
            if num>'9':
                cnt9+=1
        if cnt9>=2:
            cnt+=1
print(cnt)