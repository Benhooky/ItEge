f = open('fileforege')
k = int(f.readline())
n = f.readline()
m = int(f.readline())
s = [int(x) for x in f.readlines()]
cnt = 0
for i in range(len(s) - 2 * k):
    if (s[i] + s[i + k] + s[i + 2 * k]) % m == 0:
        cnt += 1
print(cnt)