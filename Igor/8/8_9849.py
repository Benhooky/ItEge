from itertools import product
s = product("ABCDEF", repeat=6)
listt = []
res = 0
BAD = 'AE'
for i in s:
    listt.append("".join(i))
for i in listt:
    if (i[0] not in BAD) and (i[-1] not in BAD):
        res += 1
print(res)
