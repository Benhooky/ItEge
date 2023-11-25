from itertools import product

lis = []
cnt = 0
stroki = 0
a = product("агилморф", repeat=5)
for i in a:
    lis.append("".join(i))  
for i in lis[1::2]:
    if (i[0:2] != "лм") and (i.count("и") >= 2):
        cnt += 1
print(cnt)