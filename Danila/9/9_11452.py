f = open("ItEge/Danila/9/9_11452.txt").readlines()
cnt = 0
for i in f:
    cnt += 1
    sum_nepovt = 0
    povt = 0
    a = sorted([int(x) for x in i.split()])
    if len(set(a))+1 == len(a):
        for j in set(a):
            if a.count(j) > 1:
                povt = j
            else:
                sum_nepovt += j
        if povt >= sum_nepovt/4:
            print(cnt)
            break
