f = [int(x) for x in open('ItEge/Stepan/17/17_13088 (3).txt')]
max17 = -10000
cnt = 0
maxsum = -10000
for i in f:
    if abs(i) % 100 == 17:
        max17 = max(max17, i)
for i in range(len(f)-2):
    helper = [f[i], f[i + 1], f[i + 2]]
    cnt4 = 0
    for j in helper:
        #1
        '''
        if len(str(abs(j))) == 4:
            cnt4 += 1
        '''
        #2
        if 999<abs(j)<10000:
            cnt4 += 1
    if any(abs(x) % 5 == 0 for x in helper):
        if cnt4 == 2:
            if sum(helper) > max17:
                cnt += 1
                maxsum = max(maxsum, sum(helper))
print(cnt, maxsum)