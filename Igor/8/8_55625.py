import itertools
arl = []
ar = itertools.permutations("ЯРОСЛАВ", 5)
for e in ar:
    arl.append("".join(e))

cnt = 0
sogl = "РСЛВ"
glas = "ЯОА"
BAD = []
ar = itertools.permutations(glas, 2)
for e in ar:
    BAD.append("".join(e))

for e in arl:
    if ((sum([e.count(x) for x in glas]) < sum([e.count(x) for x in sogl]))):
        if all([x not in e for x in BAD]):
            cnt += 1
print(cnt)
