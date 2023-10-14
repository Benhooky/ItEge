import itertools
ar = itertools.permutations("РУСЛАН", 6)
cnt = 0
arl = []
for e in ar:
    arl.append("".join(e))
BAD = ["УА", "АУ"]
for e in arl:
    if (all(x not in e for x in BAD)):
        cnt += 1
print(cnt)
