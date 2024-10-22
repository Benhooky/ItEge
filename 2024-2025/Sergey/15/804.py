for A in range (1,1000):
    flag=True
    for x in range (1,1000):
        if not((not(x%A==0)) <= ((x%35==0) <= (x%10==0))):
            flag=False 
            break
    if flag==True:
        print(A)