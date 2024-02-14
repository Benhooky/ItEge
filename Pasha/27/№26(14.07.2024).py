f = open('fileforege')
n = int(f.readline())
s = [int(x) for x in f.readlines()]
cnt = 0
mxsr = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) - 1):
        if (((s[i] + s[j]) / 2) in s) and (s[i] % 2 == 0 and s[j] % 2 == 0):
            cnt += 1
            mxsr = max(mxsr, ((s[i] + s[j]) / 2))
print(cnt, mxsr)
