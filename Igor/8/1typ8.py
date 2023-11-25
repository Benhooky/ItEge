import itertools
s = itertools.product("ABCDEF",repeat=6)
arl = []
cnt=0
for e in s:
    arl.append("".join(e))
for e in arl:
    if e[0]!="A" and e[0]!="E" and e[-1]!="A" and e[-1]!="E":
        cnt+=1
print(cnt)