from itertools import product
alph = '0123'
s=[]
for i in product(alph, repeat=3):
    if (i[0] != '0') and (int(i[0]) + int(i[2]) > int(i[1])):
        s.append(i)
print(len(s))