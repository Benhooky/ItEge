import time 
f = open('ItEge/Pasha/27/27B_8381.txt')
n, d, t = map(int, f.readline().split())
s = [int(x) for x in f.readlines()]
maincnt = 0
t = time.time()
for i in range(len(s) - 1):
    if i==100:
        t-=time.time()
        break
    cnt2 = 0
    if s[i] % d == 0:
        continue
    for j in range(i + 1, len(s)):
        if s[j] % d == 0:
            cnt2 += 1
        elif cnt2 == t:
            maincnt += 1
        if cnt2 > t:
            break
print(t)
print(maincnt)