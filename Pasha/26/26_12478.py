f = open('ItEge/Pasha/26/26_12478.txt')
n, st, en = map(int, f.readline().split())
s = sorted([list(map(int, x.split())) for x in f.readlines()])
sl = {}
current = st
for i in s:
    if i[0] not in sl.keys():
        sl[i[0]] = i[1]
    else:
        sl[i[0]] = max(sl[i[0]], i[1])
last = st
current = (max(x[1]-st for x in sl.items() if x[0]<=st))+st
answer2 = current
cnt = 1 
while current < en:
    a = dict(filter(lambda x: last <x[0] <= current,sl.items()))
    a = max(a.values())
    cnt+=1
    last = current
    current = a
print(cnt,answer2-1000)