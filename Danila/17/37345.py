f = [int(x) for x in open('ItEge/Danila/17/17 (9).txt')]
cnt = 0
maxSum = -10000000
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        pair = [f[i],f[j]]
        if pair[0]*pair[1]%62==0:
            cnt+=1
            maxSum = max(maxSum,sum(pair))
print(cnt,maxSum)