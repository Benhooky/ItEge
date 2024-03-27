for x in range(1,10000): 
    f = 9**1942+9*6**971+214-x
    s = ''
    d = 9
    while f>0:
        s = str(f%d) + s
        f//=d
    if abs(s.count('2') - s.count('8')) == 471:
        print(x)
        break