f = open('ItEge/Pasha/24/24_9791.txt').read()
s = ''
max0 = 0
bad = '0123456789ABCDEF'
for i in range(len(f)):
    s += f[i]
    if s[0] == '0' or s[-1] not in bad:
        max0 = max(max0, len(s) - 1)
        s = ''
if len(s) > 0:
    max0 = max(max0, len(s))
print(max0)
