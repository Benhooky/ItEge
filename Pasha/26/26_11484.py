f = open('ItEge/Pasha/26/26_11484.txt')
N = int(f.readline())
s = [[int(x) for x in d.split()] for d in f]
s = sorted(s, key=lambda x: x[1])
current = 0
cnt = 0
tmend = s[0][1]
for i in s:
    if i[0] >= current:
        current = i[1]
        cnt += 1
print(cnt, tmend)