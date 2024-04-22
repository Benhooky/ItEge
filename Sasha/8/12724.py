from itertools import product
alph = 'СПОЛКЙЕДА'
allWord = [''.join(x) for x in product(alph, repeat=6)]
cnt=-1
for word in allWord:
    cnt+=1
    if cnt%2==0:
        if word[0]!='К':
            if word.count('Й')>=2:
                if 'С' not in word and 'Е' not in word:
                    print(cnt)
                    break