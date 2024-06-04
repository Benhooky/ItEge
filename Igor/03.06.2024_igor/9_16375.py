f = open("probnik/9_16375.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int,e.split())))
    cnt2=0
    cnt1=0
    nepov=[]
    avgPovt=0
    for i in set(my_num):
        if my_num.count(i)==2:
            cnt2+=2
            avgPovt=i
        if my_num.count(i)==1:
            cnt1+=1
            nepov.append(i)
            nepov=sorted(nepov)
    if cnt2==2 and cnt1==5:
        if nepov[0]*nepov[1]*nepov[2] > avgPovt**2:
            cnt+=1
print(cnt)
        