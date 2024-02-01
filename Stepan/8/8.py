cnt = 0
from itertools import permutations
a = permutations('0124567',6)
list1 = ["".join(i) for i in a]
GOOD = ["".join(i) for i in permutations('0246',2)]
for i in list1:
    if any(x in i for x in GOOD) and i[0]!='0':
        cnt +=1
print(cnt)