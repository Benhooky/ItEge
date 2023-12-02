f = open("ItEge/Ksusha/9/9_58476.txt")
cnt = 0
for my_str in f:
    my_str = sorted([int(x) for x in my_str.split()])
    if my_str[-1] == my_str[-2]:
        continue
    my_set = set(my_str)
    if len(my_set) != len(my_str):
        if (my_str[-1] > (sum(my_str[:-1])/5) * 3):
            cnt += 1

print(cnt)
