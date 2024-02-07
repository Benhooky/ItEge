f = open('ItEge/Pasha/26/26.txt')
n = int(f.readline())
s = sorted([list(map(int, x.split())) for x in f.readlines()])
cnt = 0
sm = 0
lasttime = -1
for i in s:
    if lasttime < i[0]-1:
        sm += i[0] - lasttime - 1
        cnt += 1 
    lasttime = max(lasttime, i[1])
sm += 1439 - lasttime
cnt+=1
print(cnt, sm)