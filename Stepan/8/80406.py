from itertools import permutations
s = ["".join(i) for i in permutations('01345678', 7)]
BAD = ["".join(i) for i in permutations('0468', 2)]
c2 = ["".join(i) for i in permutations('1357', 2)]
BAD.extend(c2)
cnt = 0
for word in s:
    if word[0]!='0' and all(x not in word for x in BAD):
        cnt+=1
print(cnt)