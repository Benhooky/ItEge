f = open("ItEge/Igor/27/27A_12114.txt")
K = int(f.readline())
N = int(f.readline())
s = [int(x) for x in f.readlines()]
maxSum = 0
for i in range(0,N-K*2):
    for j in range(i+K,N-K):
        for k in range(j+K,N):
            maxSum = max(maxSum, s[i]+s[j]+s[k])
print(maxSum)