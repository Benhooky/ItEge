import itertools
s = itertools.product("РУСЛАН", repeat=5)
arl = []
cnt = 0
for e in s:
    arl.append(''.join(e))
for e in arl:
    if ((e.count("У") <= 1) and (e.count("А") <= 1)):
        cnt += 1
print(cnt)
