from itertools import product
lis = ["".join(x) for x in product('СПОЛКЙЕД',repeat = 6)]
for word in lis:
    if lis.index(word)%2==0 and word[0]=='К' and word.count('Й')>=2 and 'С' not in word and 'Е' not in word:
        print(lis.index(word))