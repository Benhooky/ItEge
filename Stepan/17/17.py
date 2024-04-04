l = [int(x) for x in open('ItEge/Stepan/17/17 (11).txt')]
count = 0
m = 0
min_25 = 100000


for num in l:
    if abs(num) % 100 == 25:
        min_25 = min(min_25, num)

for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1], l[i+2]]
    for num in s:
        if 999 < abs(num) < 10000:
            c += 1
    if c >= 2 and l[i]*l[i+1]*l[i+2] <= min_25**2:
        m = max(m, l[i]*l[i+1]*l[i+2])
        count += 1

print(count, m)

