f = [int(x) for x in open('ItEge/Stepan/17/17var04.txt')]
s = []
mini = 100000000000000
for x in range(len(f)):
    if abs(f[x]) % 1000 == 700:
        mini = min(mini, f[x])
for x in range((len(f) - 2)):
    thriple = [f[x],f[x+1],f[x+2]]
    cnt5 = 0
    for x in thriple:
        if 10000<=abs(x)<100000:
            cnt5+=1
    if cnt5<=2:
        if sum(thriple) >= mini:
            s.append(sum(thriple))
print(len(s), min(s))