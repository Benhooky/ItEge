def four(x):
    y=""
    while x>0:
        y  = str(x%4) + y 
        x//=4
    return y
for n in range(1,1001):
    i=four(n)
    if n%4==0:
        i = i + i[-2:]
    else:
        i = i + four((n%4)*2)
    r = int(i,4)
    if r >= 1088:
        print(n)
        break