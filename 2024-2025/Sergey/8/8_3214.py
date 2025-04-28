from itertools import product 
alph=product("АПРСУ",repeat=5)
lst=[]
for x in alph:
    lst.append("".join(x))
num=0
for x in lst:
    num+=1
    if x[0]=="У" and "АА" not in x:
        print(num)
        break