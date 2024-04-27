from fnmatch import fnmatch
def d(n):
    c=2
    for i in range(2,int(n**0.5)):
        if n%i==0:
            c+=2
    if n**0.5==int(n**0.5):
        c+=1
    return c
for i in range(62916,10**9,62916):
    if fnmatch(str(i),"*31*65?"):
        for x in range(1000):
            if 2**x==d(i):
                print(i,i//2031)