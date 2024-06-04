from itertools import permutations
arl = set(["".join(x) for x in permutations("СОРТИРОВКА", 10)])
BAD = ["".join(x) for x in permutations('СРРТВК', 3)]
glas = ["".join(x) for x in permutations('ООИА', 3)]
BAD.extend(glas)

cnt = 0
for word in arl:
    if all(x not in word for x in set(BAD)):
        cnt += 1
print(cnt)