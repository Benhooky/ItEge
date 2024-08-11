from itertools import product
lst = product('012345',repeat=6)
lst = ["".join(i) for i in lst]
cnt=0
for i in lst:
    if i[0] != '0' and i.count('5')<=2:
        cnt+=1
print(cnt)