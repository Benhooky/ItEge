from itertools import product
alph = '012345678'
s=[]
for i in product(alph, repeat=5):
    if  i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        s.append(i)
print(len(s))