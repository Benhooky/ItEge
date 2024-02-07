f = open('ItEge/Ksusha/26/26_13087.txt')
N = int(f.readline())
lis = [list(reversed(list(map(int,x.split())))) for x in f.readlines()]
lis = sorted(lis)
lis = [list(reversed(x)) for x in lis]
lastEnd = -1000000000
cnt=0
pool = []
for event in lis:
    if event[0]>=lastEnd+20:
        cnt+=1
        lastEnd=event[1]
        pool.append(event)
for event in lis:
    if pool[-1][0]<event[0]:
        pool[-1]=event
print(cnt,pool[-1][0]-pool[-2][1])