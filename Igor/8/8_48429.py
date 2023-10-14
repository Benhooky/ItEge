import itertools
ar = itertools.product(("012345678"), repeat=7)
arl = []
cnt = 0
for e in ar:
    arl.append("".join(e))
for e in arl:
    if (e[0] != '0' and e.count("6") == 1 and (e.count("1") + e.count("3") + e.count("5") + e.count("7")) == 2):
        cnt += 1
print(cnt)
