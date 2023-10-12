s = open("Igor\9\9_58321.txt")
cnt = 0
for my_str in s.readlines():
    my_str = my_str[:-1].split("\t")
    my_str = [int(x) for x in my_str]
    my_str.sort()
    if my_str[0] * 6 < sum(my_str[1:]):
        if my_str[-1] * my_str[0] > my_str[2] * my_str[1]:
            cnt += 1
print(cnt)
