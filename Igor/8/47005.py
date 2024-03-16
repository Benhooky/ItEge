import itertools
S = itertools.permutations("ПАРАБОЛА",8)
arl=[]
cnt=0
glas=[]
soglas=[]
ar = itertools.permutations("АО",2)
al=itertools.permutations("ПРБЛ",2)
for e in ar:
    glas.append("".join(e))
for e in al:
    soglas.append("".join(e))
for e in set(S):
    arl.append("".join(e))
glas.append('АА')
for e in arl:
    if (all(x not in e for x in glas) and all(y not in e for y in soglas)):
        cnt+=1
print(cnt)
