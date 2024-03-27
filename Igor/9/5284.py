f = open("ItEge/Igor/9/5284.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    cnt3=0
    cnt1=0
    for i in set(my_num):
        if my_num.count(i)==3:
            cnt3+=1
        if my_num.count(i)==1:
            cnt1+=1
    if ((my_num[0]+my_num[-1])**2>sum(x**2 for x in my_num[1:-1]) or 
        (cnt1==3 and cnt3==1)):
        cnt+=1
print(cnt)