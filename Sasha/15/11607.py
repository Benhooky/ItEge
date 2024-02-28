for A in range(100000,0,-1):
    flag = True
    for x in range(1,100000):
        if (not(x%263==0)<=(x%A==0))and(x%71==0):
            flag = False
            break
    if flag:
        print(A)
        break