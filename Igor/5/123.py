def tre(x):
    y=""
    while x>0:
        y+=str(x%3)
        x//=3
    return y[::-1]
min1=100000
for n in range (1,1000):
    i=tre(n)
    if n%7==0:
        i+=i[-2:]
    else:
        i+=(tre(n%7*3))
    r = int(i,3)
    if r > 369:
        min1=min(min1,r)
print(min1)