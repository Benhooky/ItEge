cnt = 0
for num, my_str in enumerate(open('ItEge/Pasha/9/9_Chai.txt'), 1):
    my_str = sorted(list(map(int, my_str[:-1].split('\t'))))
    srall = 0
    srrep = 0
    cntrep = 0
    if len(set(my_str)) != len(my_str):
        for i in set(my_str):
            if my_str.count(i) > 1:
                srrep += i * my_str.count(i)
                cntrep += my_str.count(i)
        if srrep / cntrep < sum(my_str) / len(my_str):
            cnt += num
print(cnt)
