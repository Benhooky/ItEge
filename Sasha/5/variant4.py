def f(x,system):
    s = ''
    while x>0:
        s+= str(x%system)
        x//=system
    return s[::-1]

for N in range(1,1000):
    s = f(N,4)
    if N%4 == 0:
        s += s[-2:]
    else:
        s += f(N%4 * 2,4)
    R = int(s,4)
    if R >= 1088:
        print(N)