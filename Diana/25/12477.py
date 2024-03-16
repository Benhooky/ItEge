from fnmatch import fnmatch
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1,10**7):
    if fnmatch(str(i),"3?1111*"):
        if isPrime(i):
            print(i)