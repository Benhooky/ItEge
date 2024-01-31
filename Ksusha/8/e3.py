from itertools import permutations
d=permutations('0123456789', 4)
d=[''.join(i) for i in d]
cnt=0
chet=permutations('02468',2)
chet=[''.join(i) for i in chet]
nechet=permutations('13579',2)
nechet=[''.join(i) for i in nechet]
nechet.extend(chet)
for i in d:
    if i[0]!='0' and all(s not in i for s in nechet):
        cnt+=1
print(cnt)