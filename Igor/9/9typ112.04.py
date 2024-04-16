f = open("ItEge/Igor/9/9 (1).txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    avgPovt=0
    avgUnik=0
    cnt2=0
    cnt1=0
    for digit in set(my_num):
        if my_num.count(digit)==1:
            cnt1+=1
            avgUnik+=digit
        if my_num.count(digit)==2:
            cnt2+=1
            avgPovt+=digit*2
    if cnt1==4 and cnt2==1:
        if avgUnik/4 > avgPovt/2:
            cnt+=1
print(cnt)