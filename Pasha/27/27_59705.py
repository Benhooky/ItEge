f = open('ItEge/Pasha/27/27_A (1).txt')
k = int(f.readline())
n = int(f.readline())
mn = 10000000000
s = [int(x) for x in f.readlines()]
for i in range(len(s) - 2 * k):
    for j in range(i + k, len(s) - k):
        for l in range(j + k, len(s)):
            mn = min(mn, s[i] + s[j] + s[l])
print(mn)