f = open('ItEge/Ksusha/9/9_10091.txt')
cnt = 0
for my_str in f:
    sum_povt = 0
    sred_povt = 0
    my_str = sorted([int(x) for x in my_str.split()])
    set1 = set(my_str)
    for value in set1:
        if my_str.count(value) == 2:
            sum_povt += 1
            sred_povt += value
    if sum_povt == 2 and (sred_povt/2 < sum(my_str)/7):
        cnt += 1
print(cnt)
