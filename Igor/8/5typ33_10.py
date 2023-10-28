import itertools
s = itertools.permutations("МУЖЧИНА", 6)
arl = []
cnt = 0
cnt2 = 0
for e in s:
    arl.append("".join(e))
for e in arl:
    if (e[0] != "Ч" and e.count("Ж") >= 1):
        cnt += 1
        if (cnt % 2 != 0):
            cnt2 += 1
print(cnt2)
