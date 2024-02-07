f = open('ItEge/Pasha/27/27_A.txt')
k = int(f.readline())
n = f.readline()
m = int(f.readline())
s = [int(x) for x in f.readlines()]
cnt = 0
for i in range(len(s) - 2 * k):
    for j in range(i + k, len(s) - k):
        for l in range(j + k, len(s)):
            if (s[i] * s[j] * s[l]) % m == 0:
                cnt += 1
print(cnt)