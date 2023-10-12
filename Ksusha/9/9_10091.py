f = open("Ksusha/9/9_10091.txt").readlines()
list_for_string = []
cnt = 0
for i in f:
    list_for_string.append(sorted([int(x) for x in i[:-1].split("\t")]))
for i in list_for_string:
    cntPair = 0
    avgPovt = 0
    set_for_string = set(i)
    for j in set_for_string:
        if i.count(j) == 3:
            break
        elif i.count(j) == 2:
            cntPair += 1
            avgPovt += j
    if cntPair == 2 and avgPovt/2 < sum(i)/7:
        cnt += 1
print(cnt)
