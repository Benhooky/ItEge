f = [int(x) for x in open('ItEge/Danila/17/17 (5).txt')]
cnt = 0
max1 = -100000000000000
min7 = 100000000000000000
for i in f:
    if abs(i)%10 == 7:
        min7 = min(min7,i)
for i in range(len(f)-1):
    if abs(f[i])%10 == abs(f[i+1])%10:
        if (abs(f[i])%7==0)^ (abs(f[i+1])%7==0)