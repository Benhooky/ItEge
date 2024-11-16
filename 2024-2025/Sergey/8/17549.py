from itertools import product
num = 0
f = product('КОСУФ',repeat=5)
lst = []
for x in f:
    lst.append(''.join(x))
for x in lst:
    num+=1
    if 'Ф' not in x and x.count('У')==2:
        print(num)