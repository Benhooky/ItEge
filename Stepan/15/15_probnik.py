for A in range(1000,0,-1):
    flag = True
    for x in range(1,1000):
        if not(((x%15==0)and (not(x%10==0)))<=(A<x+50)):
            flag = False
            break
    if flag:
        print(A)
        break