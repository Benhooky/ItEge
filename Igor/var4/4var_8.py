import itertools
s = itertools.product("01234567",repeat=5)
arl=[]
cnt=0
for e in s:
    arl.append("".join(e))
for e in arl:
    if int(e)%2!=0 and e[0]!="7" and (e.count("5")==1 or e.count("5")==2) and e[0]!="0":
        cnt+=1
print(cnt)