from itertools import permutations
'''
#1
alph = "СОВЕСТЬ"
s = permutations(alph,7)
lis = []
for i in s:
    lis.append(''.join(i))
'''
#2
cnt = 0
lis1 = list(set([''.join(x) for x in permutations("СОВЕСТЬ",7)]))
BAD = [''.join(x) for x in permutations("СВТ",2)]
BAD.extend(['ОЕ','ЕО'])
for word in lis1:
    if all(x not in word for x in BAD):
        cnt+=1
print(cnt)