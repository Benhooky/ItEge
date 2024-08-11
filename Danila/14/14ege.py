for x in range(1,2031):
    f = 3**100-x
    cnt0 = 0
    while f>0:
        if f%3==0:
            cnt0+=1
        f=f//3
    if cnt0==2:
        print(x)