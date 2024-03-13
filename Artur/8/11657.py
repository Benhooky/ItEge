from itertools import permutations
lis = ["".join(x) for x in permutations('0124567',6)]
good = ["".join(x) for x in permutations('0246',2)]
cnt = 0
for word in lis:
    if word[0]!='0' and any(x in word for x in good):
        cnt+=1
print(cnt)