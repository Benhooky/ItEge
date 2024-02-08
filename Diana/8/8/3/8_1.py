from itertools import permutations
arr = ["".join(x) for x in permutations("МУЖЧИНА", 6)]
number = 0
c=0
for i in arr :
    number += 1
    if i[0]!= "Ч" and i.count("Ж")>=1 and number%2==1:
        c+=1
print(c)