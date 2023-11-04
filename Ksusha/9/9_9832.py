f = open('ItEge/Ksusha/9/9_9832.txt')
for my_str in f:
    sum_povt = 0
    my_str = sorted([int(x) for x in my_str.split()])
    set1 = set(my_str)
    for value in set1:
        if my_str.count(value) == 2:
            sum_povt += 1
    if sum_povt == 2 and my_str[-2] != my_str[-1]:
        print(sum(my_str))
        break
