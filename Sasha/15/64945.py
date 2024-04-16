for A in range(100000):
    flag = True
    for x in range(100000):
        if not((x&21074!=0) <= ((x&12369==0) <= (x&A!=0))):
            flag = False
            break
    if flag:
        print(A)
        break