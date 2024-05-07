import itertools
s = itertools.product("АГЕИЛНРТ",repeat=5)
arl=[]
cnt=0
for e in s:
    arl.append("".join(e))
for i,e in enumerate(arl,1):
    if e[0]!="Т" and (e.count("Н")==1 or e.count("Н")==2):
        if i%2!=0:
            cnt+=1
print(cnt)
