from re import fullmatch
from time import time
start = time()
for x in range(23,(10**6+1),23):
    delit = 0
    for i in range(int(x**(0.5))+1,1,-1):
        if x%i==0:
            delit = max(delit,i,x//i)
    if fullmatch(r'\d{0,}6215',str(delit)):
        print(x,delit)
print(time()-start)