import itertools
s = itertools.permutations("0234567", 5)
cnt = 0
arl = []
for e in s:
    arl.append("".join(e))
s = itertools.permutations("0246", 2)
BAD = []
for e in s:
    BAD.append("".join(e))
s = itertools.permutations("357", 2)
for e in s:
    BAD.append("".join(e))
for e in arl:
    if (all(x not in e for x in BAD) and e[0] != "0"):
        cnt += 1
print(cnt)
