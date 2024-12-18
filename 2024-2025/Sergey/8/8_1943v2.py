from itertools import permutations
f = permutations('ЗЕРКАЛОККК',6)
lst = []
for x in f:
    lst.append(''.join(x))
cnt=0
for x in set(lst):
    if 1<=x.count('К'):
        cnt+=1
print(cnt)