from itertools import product 
from string import ascii_uppercase,digits
alph=(digits+ascii_uppercase)[:8]
lst=[]
pr=product(alph,repeat=7)
for x in pr:
    lst.append("".join(x))
cnt=0
chet="0246"
bad = ['17','37','57','77','75','73','71']
for x in lst:
    if x[0]!="0":
        cntChet = 0
        for digit in x:
            if digit in chet:
                cntChet+=1
        if cntChet == 2:
            if all(badElement not in x for badElement in bad):
                cnt+=1
            '''
            flag = True
            for badElement in bad:
                if badElement in x:
                    flag = False
                    break
            if flag:
                cnt+=1
            '''
print(cnt)