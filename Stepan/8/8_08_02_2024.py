from itertools import product
cnt = 0
alph = "012345678"
s = ["".join(x) for x in product(alph, repeat=5)]
BAD = ['12','32', '52', '72', '21', '23', '25', '27']
for i in s:
    if i[0]!='0' and i.count('3')== 2: 
        if all(x not in i for x in BAD):
            cnt += 1
print(cnt)