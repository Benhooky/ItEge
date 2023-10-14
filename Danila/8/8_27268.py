from itertools import permutations
a = permutations("РУСЛАН", 6)
arl = ["".join(x) for x in a]
BAD = ["АУ", "УА"]
cnt = 0
for my_str in arl:
    if all(x not in my_str for x in BAD):
        cnt += 1
print(cnt)
