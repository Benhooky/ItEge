from re import fullmatch
def f(x):
    maxDel=1
    for i in range(2,int(x**0.5)+1):
        maxDel=max(maxDel,x//i)
    return(maxDel)
for x in range(23,10**6,23):
    if fullmatch(r'\d{0,}6215',str(f(x))):
        print(x,f(x))