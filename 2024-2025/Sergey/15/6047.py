for A in range(1000):
    flag =True 
    for x in range(1000):
        for y in range(1000):
            if not((x>A) or (y>A)or ( y-2*x+12!=0)):
                flag=False 
                break 
        if flag==False:
            break
    if flag==True:
        print(A)