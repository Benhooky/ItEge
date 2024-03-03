import itertools
S = itertools.permutations("0124567",6)
arl=[]
cnt=0
chet="0246"
ar = itertools.permutations(chet,2)
BAD=[]
for e in ar:
    BAD.append("".join(e))
for e in S:
    arl.append("".join(e))
for e in arl:
    if ((any(x in e for x in BAD)) and e[0]!="0"):
        cnt+=1
print(cnt)