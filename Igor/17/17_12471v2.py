f = [int(x) for x in open("ItEge/Igor/17/17_12471 (5).txt")]
cnt=0
sred=0
max1=-200000
max13 = max(x for x in f if str(x).endswith('13')) 
for i in range(len(f)-2):
    triple = [f[i],f[i+1],f[i+2]]
    cnt2 = sum(1 for x in triple if 9<abs(x)<100)
    if all(abs(x)%2==0 for x in triple) or cnt2>0:
        if sum(triple)<=max13:
            cnt+=1
            sred += f[i]+f[i+1]+f[i+2]
print(cnt,sred//cnt)