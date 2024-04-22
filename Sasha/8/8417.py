from itertools import permutations
alph = 'ЯРОСЛАВ'
allNumbers = ["".join(x) for x in permutations(alph,  5)]
cnt = 0
sogl = 'РСЛВ'
glas = 'ЯОА'
bad = ["".join(x) for x in permutations(glas,  2)]
for word in allNumbers:
    #1
    '''
    cntSogl=0
    cntGlas=0
    for latter in word:
        if latter in sogl:
            cntSogl+=1
        if latter in glas:
            cntGlas+=1
    '''
    #2
    cntSogl = sum(1 for x in word if x in sogl)
    cntGlas = sum(1 for x in word if x in glas)
    if all(x not in word for x in bad):
        if cntSogl>cntGlas:
            cnt+=1
print(cnt)