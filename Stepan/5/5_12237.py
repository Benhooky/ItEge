for n in range(100000, 1, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += s[-2:]
    else:
        s = '1'+ s + '0'
    r = int(s, 2) 
    if r < 100:
        print(n)
        break
