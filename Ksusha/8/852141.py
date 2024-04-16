from itertools import permutations
lis=permutations('ВЕБИНАР', r=7)
cnt=[]
bad=['ВБ',"БВ","ВН","НВ","ВР","РВ","БН","НБ","БР","РБ","НР","РН","ЕИ","ИЕ","ЕА","АЕ","ИА","АИ"]
for letter in lis:
    if bad not in letter:
        cnt.append(letter)
print(cnt)#для себя
print(len(cnt))
