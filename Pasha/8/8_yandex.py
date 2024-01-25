from itertools import *
a = [''.join(j) for j in product('АЕКПТЧ', repeat=7)]
print(a.index('ПЕЧАТКА')-a.index('АПТЕЧКА')-1)