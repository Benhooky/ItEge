def F(n):
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
    return True 

from fnmatch import fnmatch
for i in range(1,10**7+1):
    if fnmatch(str(i),'3?1111*'):
        if F(i):
            print(i)
