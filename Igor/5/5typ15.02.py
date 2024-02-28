def five(x):
    i=""
    while x >0:
        i = str(x%5) + i
        x = x//5
    return i
min1=10000000
for n in range(1,1000):
    s = five(n)
    if n%25==0:
        s = s[-3:] + s
    else:
        s = s + five(n%25)
    r = int(s,5)
    if  r > 10000:
        print(n)
        break