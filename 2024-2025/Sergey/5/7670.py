minN = 10000000000000
minR = 10000000000000
for N in range(151,10000):
    n16 = hex(N)[2:]
    n16=n16.replace("a","1")
    cntChet = n16.count('0') + n16.count('2') + n16.count('4') + n16.count('6') + n16.count('8')+ n16.count('a')+ n16.count('c')+ n16.count('e')
    if cntChet > 2:
        n16+='b'
    else:
        n16 = 'f' + n16
    R = int(n16,16)
    if R > 3500:
        if minR > R:
            minR = R
            minN = N
print(minN)