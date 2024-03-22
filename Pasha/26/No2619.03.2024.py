from re import L


f = open('ItEge/Pasha/9/26_13292.txt')
n, k = map(int, f.readline().split())
s = sorted([int(x) for x in f.readlines()])
smnech = 0
last = 0
lastNumberCh = 0
lastNumberNeCh = 0
cntnch = 0
ch = []
nch = []
for i in range(k):
    if s[i]%2==0:
        ch.append(s[i])
        last=s[i]
        lastNumberCh = ch.index(last)
    else:
        nch.append(s[i])
        last=s[i]
        lastNumberNeCh = nch.index(last)
nch= nch[::-1]
lastNumberNeCh = len(nch)-lastNumberNeCh-1
if last % 2 == 0:
    lastNumber = lastNumberCh
else:
    lastNumber = lastNumberNeCh + len(ch)
ch.extend(nch)
print(lastNumber+1,sum(ch[lastNumber+1:]))