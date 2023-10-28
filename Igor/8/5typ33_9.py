import itertools
s = itertools.product("0123456", repeat=3)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))
for e in arl:
    if (e.count("1") == 1):
        cnt += 1
        if (e.count("0") == 0):
            print(cnt)
            break
