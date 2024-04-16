from string import ascii_uppercase
f=open("ItEge/Diana/24/24.3_14646.txt").readline()
keeperS = ''
res=[]
cnt3=0
dct = {}
for i in ascii_uppercase:
    dct[i] = 0
#1
#dct = {x:0 for x in ascii_uppercase}
j = 0
k = 1
while j!=len(f)-1:
    cnt3+=1
    if f[k]==f[j]:
        if cnt3>2:
            dct[f[k]]+=1 
    else:
        if cnt3>2:
            dct[f[k]]+=1
        cnt3 = 0
        j = k
    k+=1
b = sorted(dct.items(), key=lambda x: x[1], reverse=True)[0]
print(b[0],b[1],sep='')