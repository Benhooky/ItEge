f = open('ItEge/Pasha/24/24_11667.txt').readline()
s = ''
mx = 0
for i in range(len(f)):
    s += f[i]
    if s.count('INFINITY') == 1001:
        mx = max(mx, len(s) - 1)
        s = s[s.index('INFINITY') + 1:]
print(mx)