f = open('ItEge/Ksusha/9/9_9832.txt')
cnt = 0
for my_str in f:
    cnt += 1
    sum_povt = 0
    val_povt = 0
    my_str = sorted([int(x) for x in my_str.split()])
    set1 = set(my_str)
    for value in set1:
        if my_str.count(value) == 2:
            val_povt = value
            sum_povt += 1
    if sum_povt == 1 and val_povt >= (sum(my_str)-val_povt)/4:
        print(cnt)
        break
