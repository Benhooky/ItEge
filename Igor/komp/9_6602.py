f = open("ItEge/Igor/komp/6602.txt")
cnt=0
for e in f:
    my_num = sorted(list(map(int,e.split())))
    cnt1=0
    cnt2=0
    suma=0
    povtTwice=0
    povtnone=0
    for i in set(my_num):
        if my_num.count(i)==2:
            cnt2+=1
            povtTwice+=i*2
        if my_num.count(i)==1:
            cnt1+=1
            povtnone+=i
    if cnt2==1 and cnt1==4:
        if povtnone/4 >= povtTwice:
            cnt+=1
print(cnt)