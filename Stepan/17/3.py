f = [int(x) for x in open('ItEge/Stepan/17/17_9840 (1).txt')]
max_four39 = -1000000
cnt = 0
maxsum = -1000000

for num in f:
    if 1000 <= abs(num) <= 9999 and abs(num) % 100 == 39:
        max_four39 = max(max_four39, num)
for i in range(len(f) - 1):
    lst = [f[i], f[i + 1]]
    cnt4 = 0
    for x in lst:
        if 1000 <= abs(x) <= 9999:
            cnt4+=1
    if cnt4 == 1:
        if sum(lst)**2 <= max_four39**2:
            cnt+=1
            maxsum = max(maxsum, sum(lst))
print(cnt, maxsum)
