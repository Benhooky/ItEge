from itertools import permutations
f = permutations("0123456789",4)
lst=[]
for x in f: 
    lst.append(''.join(x))
cnt=0 
chet = '02468'
bad = []
for x in chet:
    for y in chet:
        bad.append(x+y)
nechet = '13579'
for x in nechet:
    for y in nechet:
        bad.append(x+y)
for elem in lst:
    if elem[0]!='0':
        if all([x not in elem for x in bad]):
            cnt+=1
print(cnt)