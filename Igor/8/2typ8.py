import itertools

s = itertools.permutations("0123456789ABCDEF", 3)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))

chet = "02468ACE"
nechet = "13579BDF"
BAD = []
ar = itertools.permutations(chet, 2)
for e in ar:
    BAD.append("".join(e))
ar = itertools.permutations(nechet, 2)
for e in ar:
    BAD.append("".join(e))

for e in arl:
    if all(x not in e for x in BAD) and e[0] != "0":
        cnt += 1
print(cnt)
