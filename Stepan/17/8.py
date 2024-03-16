f = [int(x) for x in open('ItEge/Stepan/17/17_12926 (3).txt')]
s = []
A = -100000000000
max2 = -1000000
cnt = 0
for i in f:
    if len(str(abs(i)))==2:
        max2=max(max2,i)
for i in range(0, len(f) -3):
    helper = [f[i],f[i+1],f[i+2],f[i+3]]
    if all(abs(x)%10==abs(helper[0])%10 for x in helper):
        A = max(A,sum(helper))
for i in range(0, len(f) -4):
    helper = [f[i],f[i+1],f[i+2],f[i+3],f[i+4]]
    cntA = 0
    for x in helper:
        if x<A:
            cntA+=1
    if cntA == 1 and sum(helper)%max2==0:
        cnt+=1
print(cnt)