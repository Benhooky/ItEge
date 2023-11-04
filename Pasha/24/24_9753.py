f = open('ItEge/Pasha/24/24_9753.txt').read()
s = ''
max0 = 0

for i in range(len(f)):
    s += f[i]
    if s.count('Y') == 151:
        max0 = max(max0, len(s) - 1)
        s = s[s.index('Y') + 1:]
if len(s) > 0:
    max0 = max(max0, len(s))
print(max0)
