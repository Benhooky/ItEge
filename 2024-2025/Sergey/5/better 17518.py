for N in range(1,1000):
    s=bin(N)[2:]
    if s.count('1')%2==0:
        s="10"+ s[2:] +"0"
    else:
        s="11"+s[2:]+"1"
    R=int(s,2)
    if R>50:
        print(N)
        break