for A in range (1000,1,-1):
    flag=True
    for x in range (1000):
        if not((x&51==0) or (((x&41 == 0) <= (x&A==0)))):
            flag = False
            break
    if flag:
        print(A)
        break