from itertools import product
arr =["".join(x) for x in product("АГИЛМОРТ",repeat = 5)]
number = 0
c=0
for i in arr:
    number+=1
    if number %2==1 and i[0]!="Г" and i.count("И")>=2:
        c+=1
print(c)
