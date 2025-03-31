for A in range(1,1000):
    flag=True  
    for x in range(1,1000):
        if not(((x%A==0)and(not(x%50==0)))<=(not( x%18==0) or (x%50==0))):
            flag=False
            break 
    if flag:
        print(A)
        break 

