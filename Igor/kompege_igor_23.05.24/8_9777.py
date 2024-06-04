import itertools
s = itertools.product("ЕКМОПРТЬЮ",repeat=5)
arl=[]
cnt=0
for e in s:
    arl.append("".join(e))
for i,e in enumerate(arl,1):
    if e[0]!="Ь" and e.count("К")==2:
        if (i+1)%2==0:
            print(i)
