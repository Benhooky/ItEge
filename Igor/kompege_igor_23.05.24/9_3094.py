f = open("ItEge/Igor/kompege_igor_23.05.24/9_3094.txt")
cnt=0
for e in f:
    my_num = sorted(list(map(int,e.split())))
    cnt2=0
    cnt1=0
    for i in set(my_num):
        if my_num.count(i)%2==0:
            cnt2+=my_num.count(i)//2
    if cnt2==3:
        cnt+=1
print(cnt)