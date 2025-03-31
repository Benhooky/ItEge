for A in range(1,1000):
    flag=True 
    for x in range(1,1000):
        if not(((x%A==0)and( 30<=x<=45)) <= (not(x%12==0))):
            flag=False  
            break
    if flag:
        print(A)
        break 