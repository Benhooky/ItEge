import itertools
s = itertools.product("НИКОЛАЙ", repeat=4)
cnt = 0
arl = []
for e in s:
    arl.append("".join(e))
for e in arl:
    if (((e.count("И") >= 1) or (e.count("О") >= 1) or (e.count("А") >= 1)) and (e[0] != "Й")):
        cnt += 1
print(cnt)
