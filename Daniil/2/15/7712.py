for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if ((x&17!=0)<=((x&A!=0)<=(x&58!=0)))<=((x&8==0)and(x&A!=0)and(x&58==0)):
            #значит A не подходит
            flag = False
            break
    if flag == True:
        print(A)
        break