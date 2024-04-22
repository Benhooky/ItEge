for A in range(1000):
    flag = True
    for x in range(1000):
        if not((x&39==0) or ((x&11==0) <= ((x&A)!=0))):
            flag=False
            break
    if flag:
        print(A)