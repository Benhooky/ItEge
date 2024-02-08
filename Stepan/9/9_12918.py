f = open('ItEge/Stepan/9/9_12918.txt')
arr = [sorted(list(map(int,x.split()))) for x in f]
for line in arr:
    cnt2 = 0
    cnt1 = 0
    for x in set(line):
        if line.count(x)==1:
            cnt1 += 1
        elif line.count(x)== 2:
            cnt2 += 1 
    if cnt2 == 2 and cnt1 == 2:
        if line[-1] != line[-2]:
            if line[-1] * line[0] > sum(line[1:5]):
                print(sum(line))
                break

