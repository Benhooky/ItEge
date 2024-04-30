for A in range(10000,1,-1):
    flag = True
    for x in range(1,10000):
        #if ((not(x%A==0))<=(x%26==0)<=(not(x%169==0))) == 0:
        if not((not(x%A==0)) <= ((x%26==0) <= (not(x%169==0)))):
            flag = False
            break
    if flag:
        print(A)
        break