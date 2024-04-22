from itertools import permutations
alph = 'КАБИНЕТ'
allWords = [''.join(x) for x in permutations(alph,7)]
glass = 'АИЕ'
cnt=0
for word in allWords:
    if word[-1] not in glass:
        cnt+=1
print(cnt)