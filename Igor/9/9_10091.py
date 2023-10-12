f = open("Igor/9/10091.txt").readlines()
cnt = 0
for i in f:
    my_numbers = [int(x) for x in i[:-1].split()]
    cntPairs = 0
    flag = True
    sredPovt = 0
    for j in set(my_numbers):
        if my_numbers.count(j) == 2:
            cntPairs += 1
            sredPovt += j
        elif my_numbers.count(j) > 2:
            flag = False
            break
    if cntPairs == 2 and flag:
        if sredPovt/2 < (sum(my_numbers)/7):
            cnt += 1
print(cnt)
