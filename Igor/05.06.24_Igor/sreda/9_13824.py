
f = open("ItEge/Igor/05.06.24_Igor/sreda/9.txt")
cnt=0
listansw=0
number=0
for e in f:
    number+=1
    my_num=(list(map(int, e.split())))
    flag = True
    for i in range(len(my_num)-1):
        if my_num[i]%2 == my_num[i+1]%2:
            flag=False
            break
    if flag:
        sum1 = 0
        proiz = 1
        for x in set(my_num):
            if my_num.count(x)==1:
                sum1+=x
            else:
                proiz*=x
        if 3*sum1>=proiz:
            listansw+=number
print(listansw)