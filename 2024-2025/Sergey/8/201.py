from itertools import permutations

f = permutations('ПЕСКАРЬ', 7)
lst = []
for x in f:
    lst.append(''.join(x))
cnt = 0
for word in lst:
    if word[0] != 'Ь':
        if 'ЬЕ' not in word and 'ЬА' not in word and 'ЬР' not in word:
            cnt+=1
print(cnt)