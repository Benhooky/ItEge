import itertools

s = itertools.product("ЕКМОПРТЬЮ", repeat=5)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))
for e in range(len(arl) - 1, -1, -1):
    if e % 2 == 0:
        if arl[e][0] != "Ь" and arl[e].count("К") == 2:
            print(e + 1)
            break
