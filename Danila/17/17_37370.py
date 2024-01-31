f = [int(x) for x in open('ItEge/Danila/17/17 (4).txt')]
max1 = -10000000000000000
cnt = 0
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        if abs(f[i]-f[j])%60==0:
            if abs(f[i])%15==0 or abs(f[j])%15==0:
                cnt+=1
                max1 = max(max1,abs(f[i]-f[j]))
print(cnt,max1)