f = open('ItEge/Ksusha/27/27-A_13102 (2).txt')
K = int(f.readline())
N = int(f.readline())
maxSum = -100000000
lis = [int(i) for i in f]
for i in range(len(lis)-2):
    for j in range(i+1,len(lis)-1):
        for k in range(j+1,len(lis)):
            if (j-i>=2*K) or (k-j>=2*K) or (k-i>=2*K):
                maxSum = max(maxSum,lis[i]+lis[j]+lis[k])
print(maxSum)