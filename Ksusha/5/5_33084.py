for n in range(1,10000):
    dv=bin(n)[2:]
    cnt=dv.count('1')
    dv+=str(cnt%2)
    cnt=dv.count('1')
    dv+=str(cnt%2)
    R=int(dv,2)
    if R>154:
        print(n)
        break
