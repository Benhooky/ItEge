from itertools import product
num = 0
f1 = product("ГАФНИЙ",repeat=4)
lst = []
for x in f:
    lst.append(''.join(x))
for x in lst:
    if x[0]!="Й" and (x.count("А") + x.count("И"))>=1:
        num+=1
print(num)