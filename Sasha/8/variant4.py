from itertools import product
alph = 'АГЕИЛНРТ'
allWords = ["".join(x) for x in product(alph,repeat = 5)]
cnt = 0
number = 0
for word in allWords:
    number+=1
    if number%2!=0:
        if word[0]!='Т':
            if word.count('Н')==1 or word.count('Н')==2:
                cnt+=1
print(cnt)
