from fnmatch import fnmatch
'''for x in range(10**12+2*10**11,10**13):
    if x %206==0:
        print(x)
        break
'''
from time import time
start = time()
for n in range(1200000000114,13*10**11,206):
    if n == 1200000020714:
        print(time()-start)
    if len(str(n))==13:
        if fnmatch(str(n),"12?345?67089?"):
            print(n,n/206)