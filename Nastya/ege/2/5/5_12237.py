for N in range(1000,1,-1):
    s = bin(N)[2:]
    if N%2==0:
        s+=s[-2:]
    else:
        s = '1' + s + '0'
    R = int(s,2)
    if R<100:
        print(N)
        break