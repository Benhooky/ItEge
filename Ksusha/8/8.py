from itertools import permutations
alph = "0234567"
chet = '0246'
nechet = '357'
BAD = []
strRes = []
res = permutations(alph, 5)
for i in res:
    strRes.append("".join(i))
res = permutations(chet, 2)
for i in res:
    BAD.append("".join(i))
res = permutations(nechet, 2)
for i in res:
    BAD.append("".join(i))
cnt = 0
for i in strRes:
    if i[0] != '0' and all(x not in i for x in BAD):
        cnt += 1
print(cnt)
