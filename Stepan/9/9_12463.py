f = open('ItEge/Stepan/9/9_12463.txt')
arr = [sorted(list(map(int,x.split()))) for x in f]
cnt = 0
for line in arr:
    cnt2 = 0
    cnt4 = 0
    cnt1 = 0
    avg1 = 0
    maxPovt = 0
    for x in set(line):
        if line.count(x)==1:
            cnt1+=1
            avg1+=x
        elif line.count(x)==2:
            cnt2+=1
            maxPovt = max(maxPovt,x)
        elif line.count(x)==4:
            cnt4+=1
            maxPovt = max(maxPovt,x)
    if cnt1==3 and cnt2==1 and cnt4==1:
        if avg1/3>=maxPovt:
            cnt+=1
print(cnt)