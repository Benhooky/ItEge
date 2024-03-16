f = open("ItEge/Igor/9/61389.txt")
cnt=0
for e in f:
    my_num = sorted(list(map(int, e.split())))
    if len(set(my_num)) == len(my_num):
        if (my_num[0]+my_num[-1])/2 < sum(my_num[1:-1])/4:
            cnt+=1
print(cnt)