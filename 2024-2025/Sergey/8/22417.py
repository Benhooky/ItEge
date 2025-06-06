from itertools import product 
alph=product("АБЕИЛРТФЦ",repeat=5)
lst=[]
for i in alph:
    lst.append("".join(i))
num=0
cnt=0
for x in lst:
    num+=1
    if x[0]!="А" and x[0]!="Е" and x[0]!="И":
        if x.count("Ц")==x.count("Ф"):
            if num%2!=0:
                cnt+=1
print(cnt)