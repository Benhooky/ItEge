from itertools import product
alph = 'АПРСУ'
k = 0
for x in product(alph, repeat = 4):
    k += 1
    if x[0] == 'У':
        print(k)
        break