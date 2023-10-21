import itertools
s = itertools.product("0123", repeat=3)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))
for e in arl:
    if (e[0] != "0" and ((int(e[0])+int(e[2])) > int(e[1]))):
        cnt += 1
print(cnt)
