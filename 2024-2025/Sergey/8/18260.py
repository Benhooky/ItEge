from itertools import product 
from string import ascii_uppercase, digits
cnt=0
f = product((digits+ascii_uppercase)[:12],repeat=6)
lst=[]
for x in f:
    if x[0]!="0":
        lst.append("".join(x))
lstChet="02468A"
lstNotChet="13579B"
for x in lst:
    if x.count("B")==1:
        if sum(1 for elem in x if elem in lstChet)==sum(1 for elem in x if elem in lstNotChet):
            cnt+=1
            print(x)
print(cnt)