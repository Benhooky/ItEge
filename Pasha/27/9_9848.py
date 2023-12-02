f = open('ItEge/Pasha/27/27_A_9848.txt')
k = int(f.readline())
n = int(f.readline())
s = [int(x) for x in f]
max0 = -10000000000
for i in range(len(s) - k + 1):
    for j in range(i + k, len(s) + 1):
        max0 = max(max0, sum(s[i:j]))
print(max0)