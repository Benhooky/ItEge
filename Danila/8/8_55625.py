from itertools import permutations
ar = permutations("ЯРОСЛАВ", 5)
arl = ["".join(x) for x in ar]
glas = "ЯОА"
sogl = "РСЛВ"
ar = permutations(glas, 2)
BAD = ["".join(x) for x in ar]
cnt = 0
for my_str in arl:
    if sum([my_str.count(x) for x in glas]) < sum([my_str.count(x) for x in sogl]):
        if all(x not in my_str for x in BAD):
            cnt += 1
print(cnt)
