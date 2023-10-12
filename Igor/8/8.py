from itertools import permutations
a = permutations("0234567", 5)
res = 0
s = []
for i in a:
    s.append("".join(i))
a = permutations("0246", 2)
b = permutations("357", 2)
BAD = []
for i in a:
    BAD.append("".join(i))
for i in b:
    BAD.append("".join(i))
for i in s:
    if i[0] != "0":
        if all(x not in i for x in BAD):
            res += 1
print(res)
