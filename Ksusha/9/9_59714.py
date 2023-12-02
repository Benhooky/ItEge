f = open("ItEge/Ksusha/9/59714.txt")
cnt = 0
for my_str in f:
    sred_nepovt = 0
    sred_povt = 0
    cnt_povt = 0
    my_str = sorted([int(x) for x in my_str.split()])
    my_set = set(my_str)
    flag = True
    for value in my_set:
        if my_str.count(value) == 2:
            cnt_povt += 1
            sred_povt += value
        elif my_str.count(value) > 2:
            flag = False
        else:
            sred_nepovt += value
    if flag:
        if cnt_povt == 2 and (sred_povt / 2 < sred_nepovt / 3):
            cnt += 1
print(cnt)
