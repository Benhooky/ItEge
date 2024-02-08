from itertools import product
arr = ["".join(x) for x in product("МАНГУСТ", repeat = 6)]
c=0
for i in arr:
    if i[0] !="А" and i.count("У")>=1 and i.count("М")==2:
        c+=1
print(c)
