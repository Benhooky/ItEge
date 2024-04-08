def toSmth(x,system):
    res = ''
    while x>0:
        res += str(x%system)
        x//=system
    return res[::-1]
minR = 100000000
for N in range(1,1000):
    s = toSmth(N,3)
    if N%7==0:
        s += s[-2:]
    else:
        s += toSmth(N%7*3,3)
    R = int(s,3)
    if R > 369:
        minR = min(minR,R)
print(minR)