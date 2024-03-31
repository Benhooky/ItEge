f = open('ItEge/Ksusha/27/27-A_13102 (2).txt')
maxSum = 0
K = int(f.readline())
N = int(f.readline())
lst = [int(x) for x in f]
for i in range(N-2):
    for j in range(i+1,N-1):
        for l in range(j+1,N):
            if j-i == 2*K or l-j == 2*K or l-i == 2*K:
                maxSum = max(maxSum,lst[i]+lst[j]+lst[l])
print(maxSum)