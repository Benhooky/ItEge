f=open('ItEge/Ksusha/26/26_14595 (1).txt')
n=int(f.readline())
times=sorted([[int(x) for x in line.split()] for line in f],key=lambda x:x[1])
events=[]
cLastTime=0
for time in times:
    if time[0]>cLastTime:
        events.append(time[1])
        cLastTime = time[1]
        if len(events)%3==0:
            cLastTime+=10
print(len(events))
            