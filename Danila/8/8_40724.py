from itertools import permutations
a = permutations("СВЕТЛАНА", 8)
arl = ["".join(x) for x in a]
cnt = 0 
for my_str in set(arl):
    if "АА" not in my_str:
        cnt += 1
print(cnt)