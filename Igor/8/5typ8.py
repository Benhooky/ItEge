import itertools
s = itertools.product("УДАЧ",repeat=5)
arl = []
cnt=0
for e in s:
    arl.append("".join(e))
for e in arl:
    if e[0]=="А":
        cnt+=1
print(cnt)