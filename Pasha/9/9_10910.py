cnt = 0

for my_str in open("ItEge/Pasha/9/9_10910.txt"):
    my_str = sorted(list(map(int, my_str[:-1].split('\t'))))
    if my_str[0] != my_str[1] and len(set(my_str)) < 6:
        summ = 0
        if sum(list(filter(lambda x: my_str.count(x) > 1, my_str))) > my_str[0] + my_str[-1]:
            cnt += 1
print(cnt)
