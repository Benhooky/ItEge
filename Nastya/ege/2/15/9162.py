def ПЛОЩ(a,b,c):
    if (a*b)>c:
        return True
    else:
        return False
    
for A in range(1000, -1000, -1):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((not(ПЛОЩ(x, y, A+13))) <= ПЛОЩ(28, y, 520) or ПЛОЩ(x, 25, 800)):
                flag= False
                break
        if flag == False:
            break
    if flag:
        print(A)
        break
