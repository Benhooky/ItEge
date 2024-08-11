for N in range(1, 10000):
    s = bin(N)[2:]
    if s.count('1') % 2 == 0:
        s += '0' 
        s = '10' + s[2:]
    else:
        s += '1' 
        s = '11' + s[2:]
    r = int(s, 2)
    if r<35:
        print(N)