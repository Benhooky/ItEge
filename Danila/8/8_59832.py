from itertools import product
a = product("012345678", repeat=5)
arl = ["".join(x) for x in a if x[0] != "0"]
BAD = []
for i in '1357':
    BAD.append('2' + i)
    BAD.append(i + '2')
cnt = 0
for my_mynbr in arl:
    if (my_mynbr.count("3") == 2) and all(x not in my_mynbr for x in BAD):
        cnt += 1
print(cnt)