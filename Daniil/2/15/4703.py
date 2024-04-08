for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if not(((x%2==0)<=(not(x%3==0)))or(x+A>=100)):
            #значит A не подходит
            flag = False
            break
    if flag == True:
        print(A)
        break