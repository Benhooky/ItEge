from itertools import permutations
count = 0
bad1 = [''.join(i) for i in list(permutations('0246', 2)
                                 )+(list(permutations('357', 2)))]
for i in permutations('0234567', 5):
    i = ''.join(i)
    if i[0] != '0' and all(x not in i for x in bad1):
        count += 1
print(count)
