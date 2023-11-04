f = open('ItEge/Pasha/24/24_9850.txt').read()
s = f
bad = 'LISENOK'
max0 = 0
for i in bad:
    s = s.split(i)
    s = '|'.join(s)
s = s.split('|')
s = sorted(s, key=len, reverse=True)
print(len(s[0]))
