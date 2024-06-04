f = open("dz/9_3887.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int, e.split())))
    sredn=sum(my_num)/len(my_num)
    cntBIG=0
    for digit in my_num:
        if digit > sredn:
            cntBIG+=1
    if cntBIG >=3:
        cnt+=1
print(cnt)