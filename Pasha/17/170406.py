spis = [int(x) for x in open('ItEge/Pasha/17/17 (15).txt')]
cnt = 0
sm = -1000000000
mn = 10000000000000
def thr(a):
    return abs(a) in [x for x in range(100, 1000)]
def four(b):
    return abs(b) in [x for x in range(1000, 10000)]
for i in spis:
    if (i > 0) and (four(i)) and (str(i)[-1] == str(i)[-2]):
        mn = min(mn, i)
for j in range(len(spis) - 2):
    timeSpis = [spis[j], spis[j + 1], spis[j + 2]]
    if all(thr(l) for l in timeSpis):
        if sum(timeSpis) > mn:
            cnt += 1
            sm = max(sm, sum(timeSpis))
print(cnt, sm)