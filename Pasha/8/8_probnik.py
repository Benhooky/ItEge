from itertools import *
cnt = 0
for i in product('АЗИМНОПРТ', repeat=5):
    cnt += 1
    i = ''.join(i)
    if i[0] == 'Н' and i.count('Р') == 2 and cnt%2==0:
        print(i, cnt)