from itertools import product
from string import ascii_uppercase,digits
alph = (digits+ascii_uppercase)[:8]
lst = []
pr = product(alph,repeat = 5)
for x in pr:
    if x[0]!='0':
        lst.append(''.join(x))
cnt = 0
for x in lst:
    if x[0] == '0' or x[0]=='2' or x[0]=='4' or x[0]=='6':
        if x[-1] != '2' and x[-1] != '6':
            if x.count('7')<=2:
                cnt+=1
print(cnt)