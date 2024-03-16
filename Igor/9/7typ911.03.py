f = open("dz/9(11.03).txt")
cnt=0
for e in f:
    my_num = sorted(list(map(int, e.split())))
    if len(set(my_num)) == 5:
        flag = 1
        sr1 = 0
        for i in range (0,len(my_num)):
            if my_num.count(my_num[i]) == 2:
                sr1 += my_num[i]
            if my_num.count(my_num[i]) > 2:
                flag = 0
                break
        if flag == 1:
            sr2 = (sum(my_num)-sr1)/3
            sr1 = sr1/4
            if sr2 < sr1:
                cnt += 1
print(cnt)