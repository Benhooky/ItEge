f=open('ItEge/Ksusha/26/26_10107 (2).txt')
N=int(f.readline())
times = sorted([[int(x) for x in line.split()] for line in f],key = lambda x:x[1])
currentLastTime = times[0][1]
cnt = 1
listOfEvents = []
answerList = []
for event in times[1:]:
    if event[0]>=currentLastTime:
        cnt+=1
        listOfEvents.append(event[1])
        currentLastTime=event[1]
for event in times:
    answerList.append(event[0]-listOfEvents[-2])
print(cnt,max(answerList))