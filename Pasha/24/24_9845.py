from itertools import product
f = open('ItEge/Pasha/24/24_9845.txt').read()
s = f[0]
b = len(f)
bad = [''.join(x) for x in product('89', repeat=2)]
bad2 = [''.join(j) for j in product('ABC', repeat=2)]
bad.extend(bad2)
max0 = 0
for i in range(len(f)):
    s += f[i]
    if (s[-2:]) in bad:
        max0 = max(max0, len(s) - 1)
        s = s[-1]
if len(s) > 1:
    max0 = max(max0, len(s))
print(max0)
