f= open("ItEge/Igor/04.06.2024_igor/9 (2).txt")
listsum=0
number = 0
for e in f:
    number += 1
    my_num=sorted(list(map(int, e.split())))
    cnt1=0
    for i in set(my_num):
        if my_num.count(i)==1:
            cnt1+=1
    if cnt1==6:
        if (my_num[-1] - my_num[0])**3 >= (my_num[1] + my_num[2] + my_num[3] + my_num[4])**2:
            listsum+=number
print(listsum)