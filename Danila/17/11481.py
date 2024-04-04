f = [int(x) for x in open('ItEge/Danila/17/17_11481 (1).txt')]
max8= max(x for x in f if str(abs(x))[0] == '8')
cnt=0
min3=1000000000000
for i in range(len(f)-2):
    triple = [f[i],f[i+1],f[i+2]]
    cnt6=sum(1 for x in triple if str(abs(x))[0] == '6')
    if cnt6<=1:
        if sum(triple)>=max8:
            cnt+=1
            min3=min(min3,sum(triple))
print(cnt,min3)
