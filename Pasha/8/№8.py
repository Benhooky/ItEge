from itertools import *
cnt = 0
a = []
flag = False
for i in [''.join(j) for j in product('АЕКПТЧ', repeat=7)]:
    if flag:
        cnt += 1
    if i == 'АПТЕЧКА' :
        flag = True
    if i == 'ПЕЧАТКА':
        flag = False
        break

print(cnt)