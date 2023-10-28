import itertools
s = itertools.product("ABCX", repeat=5)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))
for e in arl:
    if e.count("X") == 0 or e.count("X") == 1 and e[-1] == "X":
        cnt += 1
        print(e)
print(cnt)
