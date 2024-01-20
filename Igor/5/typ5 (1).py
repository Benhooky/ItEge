min1=1000000
for n in range (1,10000):
    i = bin(n)[2:]
    if n%8==0:
        i+=i[-2:]
    else:
        n1 = (n%8)*2
        i+=bin(n1)[2:]
    r = int(i,2)
    if r>3000:
        print(n)
        break