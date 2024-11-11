for x in range(1,1000):
    res = 64**11-4**10+96-x
    s = ''
    while res != 0:
        s += str(res%4)
        res //= 4
    s = s[::-1]
    sum1 = 0
    for i in s:
        sum1 += int(i)
    if sum1 == 71:
        print(x)
        break