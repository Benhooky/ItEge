for x in range(1,100000):
    res = 4**2015+2**x-2**2015+15
    res = bin(res)[2:]
    if res.count('1') == 500:
        print(x)
        break