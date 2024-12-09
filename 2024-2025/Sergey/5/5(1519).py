for N in range(66,10000):
    s = bin(N)[2:]
    for i in range(3):
        cnt0 = s.count('0')
        cnt1 = s.count('1')
        if cnt0 == cnt1:
            s = s+s[-1]
        elif cnt0 < cnt1:
            s = s +'0'
        else:
            s = s + '1'
    R = int(s,2)
    if R%4==0:
        print(N)
        break