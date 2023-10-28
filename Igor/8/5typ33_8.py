import itertools
s = itertools.product("ABCDXYZ", repeat=4)
arl = []
cnt = 0

for e in s:
    arl.append("".join(e))
s = "XYZ"
s1 = "ABCD"
for e in arl:
    if e[0] in s and e[1] in s and e[2] in s1 and e[3] in s1:
        cnt += 1
print(cnt)
