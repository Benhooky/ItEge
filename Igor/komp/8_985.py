import itertools
s = itertools.permutations("БИТКОИН",7)
cnt=0
arl=[]
for e in s:
    arl.append("".join(e))
arl = set(arl)
for e in arl:
    cnt+=1
print(cnt)