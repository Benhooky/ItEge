import itertools
ar = itertools.permutations(("0123456789"), 6)
arl = []
cnt = 0
for e in ar:
    arl.append("".join(e))
chet = "02468"
neChet = "13579"
BAD = []
ar = itertools.permutations(chet, 2)
for e in ar:
    BAD.append("".join(e))
ar = itertools.permutations(neChet, 2)
for e in ar:
    BAD.append("".join(e))
for e in arl:
    if int(e) % 5 == 0:
        if (e[0] != '0' and all(x not in e for x in BAD)):
            cnt += 1
print(cnt)
