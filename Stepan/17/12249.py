f = [int(x) for x in open('ItEge/Stepan/17/17_12249 (2).txt')]
cnt = 0
max5 = -100000000000
maxSum = -10000000000
for i in f:
    if len(str(abs(i))) == 5 and abs(i)%10==3:
        max5 = max(max5, i)
for i in range(len(f)-2):
    r = [f[i],f[i+1],f[i+2]]
    if any(abs(x)%10 == 3 for x in r):
        if sum(r)<=max5:
            cnt+=1
            maxSum = max(maxSum, sum(r))
print(cnt,maxSum)