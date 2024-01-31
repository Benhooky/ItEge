from itertools import product
d=product('вишня', repeat=6)
d=["".join(i) for i in d]
cnt=0
for i in d:
    if i.count('в')<2 and i[0]!='ш' and i[-1]!='я' and i[-1]!='и':
        cnt+=1
print(cnt)