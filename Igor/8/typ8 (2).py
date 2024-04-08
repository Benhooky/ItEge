import itertools
s = itertools.product("АЗИМНОПРТ",repeat=5)
arl=[]
cnt=0
for e in s:
    arl.append("".join(e))
for number,e in enumerate(arl,1):
    if e[0]=="Н" and e.count("Р")==2 and number%2==0:
            print(number)