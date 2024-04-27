def f(x):
    s=''
    while x>0:
        s=str(x%4)+s
        x=x//4
    return s
for n in range(1,1000):
    s4 = f(n)
    if n%4==0:
        s4+=f(n)[-2:]
    else:
        s4+=f(n%4*2)
    r = int(s4,4)
    if r>=1088:
        print(n,r)
print("Ответ:20")