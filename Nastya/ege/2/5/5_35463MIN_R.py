minR=1000000000000000
for N in range(1,1000):
    s = bin(N)[2:]
    for i in range(3):
        cnt0 = s.count('0')
        cnt1 = s.count('1')
        if cnt0 == cnt1:
            s += s[-1]
        else:
            if cnt0 > cnt1:
                s+='1'
            else:
                s+='0'
    R = int(s,2)
    if (R>50) and (R % 4 == 0):
        minR = min(minR,R)
print(minR)