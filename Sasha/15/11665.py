for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if not((A+x>700-A)and((A%100+100%x)>50)):
            flag = False
            break
    if flag:
        print(A)
        break