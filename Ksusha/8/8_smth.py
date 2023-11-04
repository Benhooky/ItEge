from itertools import product
cnt = 0
s = product("0123456789ABC", repeat=6)
slist = []
for i in s:
    if i.count('5') <= 1 and i[0] != '0':
        slist.append(''.join(i))
s = product("13579B", repeat=2)
bad = []

for i in s:
    bad.append(''.join(i))
for i in slist:
    if all(x not in i for x in bad):
        cnt += 1
        print(i)
print(cnt)
