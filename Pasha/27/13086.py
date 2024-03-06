f = open('ItEge/Pasha/27/27-A_13086.txt')
k = int(f.readline())
n = int(f.readline())
s = [int(x) for x in f.readlines()]
print(s)
mx = -10000000000
for i in range(len(s) - 2 * k):
    for j in range(i+1, len(s) - 2* k):
        for l in range(i + 2*k, len(s)):
            mx = max(mx, s[i] + s[j] + s[l])
print(mx)