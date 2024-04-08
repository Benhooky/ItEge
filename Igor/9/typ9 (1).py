f = open("ItEge/Igor/9/9.txt")
cnt=0
max1=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    f1 = len(set(my_num))==len(my_num)
    f2 = (my_num[0]+my_num[-1])*2 <= sum(my_num[1:-1])*3
    if f1 and not f2 or f2 and not f1:
        cnt+=1
print(cnt)