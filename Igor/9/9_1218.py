f = open("ItEge/Igor/9/9_1218.txt")
cnt=0
for e in f:
    my_num = sorted(list(map(int , e.split())))
    cnt1=0
    cnt2=0
    for i in set(my_num):
        if my_num.count(i)==2:
            cnt2+=1
        if my_num.count(i)==1:
            cnt1+=1
    if cnt2==2 and cnt1==2:
        if my_num[-1] != my_num[-2]:
            if (my_num[-1]*my_num[0])>sum(my_num[1:-1]):
                print(sum(my_num))
                break

