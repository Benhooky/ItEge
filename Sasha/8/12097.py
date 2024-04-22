from itertools import product
alph = 'АГДИЛНРЯ'
allWords = [''.join(x) for x in product(alph, repeat = 6)]
cnt = 0
for word in allWords:
    cnt+=1
    if cnt%2==0:
        if word[0]!='Я' and word.count('Д')==3:
            print(cnt)