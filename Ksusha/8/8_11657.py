from itertools import *
d=permutations('01234567',6)
cnt=0
d=[''.join(x) for x in d if x[0]!="0" and '3' not in x]
good=[''.join(x) for x in product('0246',repeat=2)]
for x in d:
    if any(s in x for s in good):
        cnt+=1
print(cnt)
