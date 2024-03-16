from itertools import permutations
s1 = 'ПРБЛ'
s2 = 'АО'
count = set()
for var in permutations('ПАРАБОЛА', 8):
    slovo = ''.join(var)
    if all((slovo[i] in s1 and slovo[i+1] in s2) or (slovo[i+1] in s1 and slovo[i] in s2) for i in range(len(slovo)-1)):
        count.add(slovo)
print(len(count))