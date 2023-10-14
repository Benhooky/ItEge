from itertools import product
a = product("012345678", repeat=7)
arl = ["".join(x) for x in a]
neChet = '1357'
cnt = 0
for my_str in arl:
    if (my_str.count("6") == 1) and (len([x for x in my_str if x in neChet]) == 2) and my_str[0] != '0':
        cnt += 1
print(cnt)
