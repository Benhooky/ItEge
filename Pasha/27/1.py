f = open('Pasha/27/27_A_9755.txt')
K = int(f.readline())
N = int(f.readline())
s = [int(x) for x in f]
min0 = 10000000000000000000000000000
for i in range(len(s) - K):
    for j in range(i + K, len(s) - K):
        for l in range(j + K, len(s)):
            min0 = min(min0, s[i] + s[j] + s[l])
print(min0)
