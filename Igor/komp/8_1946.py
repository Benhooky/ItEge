import itertools
s=itertools.product("01234",repeat=5)
cnt=0
arl=[]
for e in s:
    arl.append("".join(e))
for e in arl:
    if ( ((e.count("0") + e.count("2") + e.count("4"))<=3) and e[0]!="0" ):
        cnt+=1
print(cnt)