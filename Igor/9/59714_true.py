f = open('ItEge/Igor/9/9_59714.txt')
cnt = 0
for s in f:
    a = sorted(list(map(int, s.split())))
    cnt2 = 0 # 2
    cnt1 = 0 # 3
    avgPovt = 0
    avgNePovt = 0 
    for value in set(a):
        if a.count(value)==2:
            cnt2+=1
            avgPovt+=value*2
        if a.count(value)==1:
            cnt1+=1 
            avgNePovt+=value
    if cnt2==2 and cnt1==3:
        if avgPovt/4 < avgNePovt/3:
            cnt+=1
print(cnt)