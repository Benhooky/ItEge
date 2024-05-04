file = open('ItEge/Pasha/24/24var04.txt').readline()
s = ''
mx = -10000000000000
for i in range(len(file)):
    s += file[i]
    if s.count('A') == 701 or s[-1] == 'E':
        if s.count('A') == 701:
            mx = max(mx, len(s) - 1)
            s = s[s.index('A')+1:]
        if s[-1] == 'E':
            mx = max(mx, len(s) - 1)
            s = ''
if len(s) > 0:
    mx = max(mx, len(s))
print(mx)