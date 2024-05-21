f = open('ItEge/Diana/26/26_2024 (1).txt')
N = int(f.readline())
lst = sorted([[int(y) for y in x.split()] for x in f],key = lambda x: x[1])
currentEnd = 0
cnt=0
for event in lst:
    if event[0]>=currentEnd:
        cnt+=1
        currentEnd=event[1]
print(cnt)