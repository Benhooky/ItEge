f = open('ItEge/Pasha/27/27A_11673.txt')
k = int(f.readline())
n = int(f.readline())
s = [int(x) for x in f.readlines()]
cnt = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[j] - s[i] > k:
            cnt += 1
print(cnt * 2)