from itertools import permutations
list1 = ["".join(i) for i in permutations("0234567",5)]
BAD1  = ["".join(i) for i in permutations("0246",2)]
BAD2 = ["".join(i) for i in permutations("357",2)]
cnt = 0
BAD1.extend(BAD2)
for i in list1:
    if all(x not in i for x in BAD1) and i[0]!="0"  :
        cnt+=1
print(cnt)