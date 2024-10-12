for A in range (1000):
    flag = True
    for x in range (1000):
        for y in range (1000):
            if not ((x<=19) or (y < 2*x + A - 50) or ( y>17)):
                flag = False
                break 
        if flag==False:
            break
    if flag==True:
        print(A)
        break
