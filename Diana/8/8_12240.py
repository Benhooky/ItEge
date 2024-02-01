from itertools import product
list1 = ["".join(i) for i in product("012345678",repeat = 5)]
BAD1  = ["00", "11","22","33","44","55","66","77","88"]
cnt = 0
for i in list1:
    if all(x not in i for x in BAD1) and i[0]!="0" and i.count("5")==1 :
        cnt+=1
print(cnt)