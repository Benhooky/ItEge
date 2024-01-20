import itertools
arl = ["".join(e) for e in itertools.product("АГДИЛНРЯ",repeat=6)]
cnt=0
for i in range(len(arl)):
    if (arl[i][0]!="Я" and arl[i].count("Д")==3 and (i+1)%2==0):
        cnt = i+1
print(cnt)
