import itertools
s = itertools.product("ВИШНЯ",repeat=6)
arl = []
cnt = 0
for e in s:
    arl.append("".join(e))
for e in arl:
    if (e[0]!="Ш" and e[5]!="И" and e[5]!="Я" and e.count("В")<=1):
        cnt+=1
print(cnt)