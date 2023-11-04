f = open('ItEge/Ksusha/9/today.txt')
cnt = 0
for my_str in f:
    sum_povt = 0
    my_str = sorted([int(x) for x in my_str.split()])
    if my_str[0] != my_str[1]:
        set1 = set(my_str)
        if len(my_str) != len(set1):
            for value in set1:
                if my_str.count(value) > 1:
                    sum_povt += value*my_str.count(value)
            if my_str[0]+my_str[-1] < sum_povt:
                cnt += 1
print(cnt)
