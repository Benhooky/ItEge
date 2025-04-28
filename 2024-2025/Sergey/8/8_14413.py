from itertools import permutations
alph="СОРТИРОВКА"
pr= permutations(alph,10)
lst=[]
for x in set(pr):
    lst.append("".join(x))
bad=[]
pr=permutations("СРТРВК",3)
for x in pr:
    bad.append("".join(x))
pr=permutations("ОИОА",3)
for x in pr:
    bad.append("".join(x))
bad = list(set(bad))
cnt=0
for x in lst:
    if all([elem not in x for elem in bad]):
        cnt+=1
print(cnt)