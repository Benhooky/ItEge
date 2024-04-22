from re import fullmatch
from time import time
start = time()
for x in range(23,(10**6+1),23):
    delit = 0
    if x%2==1:
        for i in range (x//2+1,0,-1):
            if x%i==0:
                delit=i
                break
    if x%2==0:
        delit=x//2
    if fullmatch(r'\d{0,}6215',str(delit)):
        print(x,delit)
print(time()-start)