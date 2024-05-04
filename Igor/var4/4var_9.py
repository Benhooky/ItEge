f = open("probnik/9.txt")
max1=0
cnt=0
for e in f:
    my_num=sorted(list(map(int , e.split())))
    cnt4=0
    cnt2=0
    cnt1=0
    avgPovt2=0
    avgPovt=0
    avgPovt4=0
    tipi=0
    for i in set(my_num):
        if my_num.count(i)==4:
            cnt4+=1
            avgPovt4=i
        if my_num.count(i)==2:
            cnt2+=2
            avgPovt2=i
        if my_num.count(i)==1:
            cnt1+=1
            tipi+=i
        avgPovt=max(avgPovt2,avgPovt4)
    if cnt4==1 and cnt1==2 and cnt2==1:
        if tipi/2 >= avgPovt:
            cnt+=1
print(cnt)