for N in range(3,10000):
    x = N
    s = ''
    while x > 0:
        s+=str(x%3)
        x=x//3
    s=s[::-1]
    if N%3==0:
        s+=s[-2:]
    else:
        x = N%3*3
        g = ''
        while x > 0:
            g+=str(x%3)
            x=x//3
        g=g[::-1]
        s+=g
    R=int(s,3)
    if R<=150:
        print(N)