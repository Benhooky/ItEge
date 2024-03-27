f = open("ItEge/Igor/9/9_12797.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    cnt1=0
    cnt2=0
    for i in set(my_num):
        if my_num.count(i)==2 and i%2==0:
            cnt2+=1
        if my_num.count(i)==1 and i%2!=0:
            cnt1+=1
    if cnt2==1 and cnt1==2:
        cnt+=1
print(cnt)