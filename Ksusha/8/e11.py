from itertools import permutations
d=permutations('0234567', 5)
cnt=0
chet=permutations('0246',2)
chet=[''.join(x) for x in chet]
nechet=permutations('1357',2)
nechet=[''.join(x) for x in nechet]
d=[''.join(x) for x in d]
for x in d:
    if x[0]!='0' and (all(s not in x for s in chet)) and (all(s not in x for s in nechet)):
        cnt+=1
print(cnt)

