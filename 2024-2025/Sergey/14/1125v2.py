for x in range(1,1000):
    res = 64**11-4**10+96-x
    sum1 = 0
    while res != 0:
        sum1 += res%4
        res //= 4
    if sum1 == 71:
        print(x)
        break