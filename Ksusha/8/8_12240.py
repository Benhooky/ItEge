from itertools import product
c=0
d=product('012345678',repeat=5)
d=[''.join(x) for x in d]
Bad=[str(i)+str(i) for i in range(0,9)]
for i in d:
    if i.count('5')==1 and all([x not in i for x in Bad]):
        if i[0]!='0':
            c+=1
print(c)
