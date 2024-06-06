from fnmatch import fnmatch
from time import time
start = time()
for i in range(2658,10**9,2658):
    if fnmatch(str(i),'85?16*4'):
        print(i,i//2658)
print(time()-start)