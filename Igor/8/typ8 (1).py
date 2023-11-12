import itertools

s = itertools.product("012345678", repeat=5)
cnt = 0
arl = []
for e in s:
    arl.append("".join(e))
BAD = ['35','53','36','63','73','37','83','38']
for e in arl:
    if (
        e.count("3") == 1
        and all(x not in e for x in BAD)
        and e[0] != "0"
    ):
        cnt += 1
print(cnt)
