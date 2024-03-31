f = [int(x) for x in open("ItEge/Igor/17/17_12471 (5).txt")]
cnt=0
sred=0
max1=-200000
max13 = max([x for x in f if str(x).endswith('13')]) 
for i in range(len(f)-2):
    if ( ((f[i]%2==0 and f[i+1]%2==0 and f[i+2]%2==0)
        or ((len(str(f[i]))==2) or (len(str(f[i+1]))==2) or (len(str(f[i+2]))==2)) )
        and ((f[i] + f[i+1] + f[i+2])<=max13)): 
        cnt+=1
        sred += f[i]+f[i+1]+f[i+2]
print(cnt,sred//cnt)