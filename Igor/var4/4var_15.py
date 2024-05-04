for A in range(1,1000):
    flag=True
    for x in range(1,1000):
        for y in range(1,1000):
            if not( (x >= 20) or (y >= 40) or (y <= x + A) or (y >= 3*x - A)):
                flag=False
    if flag:
        print(A)
        break