from itertools import product
a = product("012345678", repeat = 5)
arl = ["".join(x) for x in a]

BAD = ['53','51','57','35','15','75']
cnt = 0
for number in arl:
    if number.count('5')==1 and all(x not in number for x in BAD) and number[0]!='0':
        cnt+=1
print(cnt)