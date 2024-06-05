from itertools import *
S = product("01234567",repeat=5)
cnt=0
arl=[]
Good = []
for i in range(8):
    Good.append(str(i)*3)
for e in S:
    arl.append("".join(e))
for slovo in arl:
    if slovo[0]!='0':
        if any(x in slovo for x in Good):
            if len(set(slovo))==3:
                cnt+=1
print(cnt)