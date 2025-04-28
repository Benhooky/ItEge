from itertools import product
s = product('АЕИКМСЧ', repeat = 5)
lst = []
for x in s:
    lst.append("".join(x))
print(lst.index('ЧЕЧИК')-lst.index('МАСИК')-1)