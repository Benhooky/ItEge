from itertools import product
a = product("ABCDEF", repeat=6)
aList = []
cnt = 0
for i in a:
    aList.append("".join(i))
for i in aList:
    if i[0] != 'A' and i[0] != 'E' and i[-1] != 'A' and i[-1] != 'E':
        cnt += 1
print(cnt)
