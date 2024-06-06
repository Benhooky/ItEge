for A in range(1000):
    flag=True
    for x in range(1000):
        if not(((x&52!=0) and (x&36 ==0))<= (not(x&A==0))):
            flag=False
    if flag:
        print(A)
        break