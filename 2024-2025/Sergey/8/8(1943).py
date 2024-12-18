from itertools import product
f = product('ЗЕРКАЛО',repeat=6)
lst = []
for x in f:
    lst.append(''.join(x))
cnt=0
for x in lst:
    if 1<=x.count('К')<=4 and x.count('З')<=1 and x.count('Е')<=1 and x.count('Р')<=1 and x.count('А')<=1 and x.count('Л')<=1 and x.count('О')<=1:
        cnt+=1
print(cnt)