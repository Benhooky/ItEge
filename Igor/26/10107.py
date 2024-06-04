
f=open('ItEge/Igor/26/26_10107 (1).txt')
N = int(f.readline())
events = sorted([[int(x) for x in line.split()] for line in f],key = lambda lst: lst[1])
currentEndTime = events[0][1]
cnt = 1
lastE = 0
lastTimeEnd = 0
maxDelay = 0
for e in events[1:]:
    if e[0]>=currentEndTime:
        cnt+=1
        lastE = events.index(e)
        lastTimeEnd = currentEndTime
        currentEndTime = e[1]
for e in events[lastE:]:
    if e[0]>lastTimeEnd:
        maxDelay = max(maxDelay,e[0]-lastTimeEnd)
print(cnt,maxDelay)