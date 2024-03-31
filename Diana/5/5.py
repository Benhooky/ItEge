def f(n):
    s=""
    while n>0:
        s=str(n%3)+s
        n=n//3
    return s
r=0
minR = 1000000000
for n in range(1,1000):
    if n%7==0:
        r=int((f(n)+f(n)[-2:]),3)
    else:
        r=int((f(n)+f(n%7*3)),3)
    if r>369:
        minR = min(minR,r)
print(minR)