f = open("ItEge/Ksusha/9/9_11452.txt")
cnt = 0
for my_numbers in f:
    cnt += 1
    s = sorted([int(x) for x in my_numbers.split()])
    povt = 0
    sum_povt = 0
    if len(set(s)) == 5:
        for j in set(s):
            if s.count(j) > 1:
                povt = j
            else:
                sum_povt += j
        if povt >= sum_povt / 4:
            print(cnt)
            break
