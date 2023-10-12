f = open("Danila/9/09_9156.txt")
cnt = 0
for my_str in f.readlines():
    my_str = my_str[:-1].split("\t")
    my_list = [int(x) for x in my_str]
    my_list.sort()
    if (my_list[0]+my_list[3]) % 3 == 0:
        if (my_list[3]-my_list[2] == my_list[1]-my_list[0]) or (my_list[3]-my_list[1] == my_list[2]-my_list[0]):
            cnt += 1
print(cnt)
