f = open("ItEge/Igor/komp/6897.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    if my_num[3]<my_num[0]+my_num[1]+my_num[2]:
        if (my_num[0]+my_num[3])!=(my_num[1]+my_num[2]):
            cnt+=1
print(cnt)