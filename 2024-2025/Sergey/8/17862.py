from string import ascii_uppercase,digits
from itertools import product
alph = (digits + ascii_uppercase)[:12]
pr = product(alph,repeat = 5)
lst = []
cnt = 0
for x in pr:
    lst.append(''.join(x))
for number in lst:
    cnt8 = 0
    if number[0]!='0':
        if number.count('7')==1:
            for digit in number:
                if int(digit,12) > 8:
                    cnt8+=1
            if cnt8 <= 3:
                cnt+=1
print(cnt)