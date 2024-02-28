f = open('C:/Users/Dell/Downloads//24_11667.txt').readline()
f = f.replace('INFINITY', '*')
s = ''
mx = 0
for i in range(len(f)):
    s += f[i]
    if s.count('*') == 1001:
        mx = max(mx, len(s) - 8)
        s = s[s.index('*') + 1:]
print(mx)