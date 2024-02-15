from itertools import product
arr = ["".join(x) for x in product("012345678",repeat =5)]
bad= ["12","32","52","72","92","21","23","25","27","29"]

cnt=0
for i in arr:
    if  i[0]!="0" and i.count("3")==2 and (all(x not in i for x in bad)):
        cnt+=1
print(cnt)
