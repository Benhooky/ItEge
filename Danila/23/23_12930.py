from functools import lru_cache 
from time import time
@lru_cache
def f1(from1, to1):
    if from1 > to1 or from1 == 11 or from1 == 12:
        return 0
    if from1 == to1:
        return 1
    if from1 < to1:
        return f1(from1+1, to1) + f1(from1*2, to1) + f1(from1**2, to1)
    
def f2(from1, to1):
    if from1 > to1 or from1 == 11 or from1 == 12:
        return 0
    if from1 == to1:
        return 1
    if from1 < to1:
        return f2(from1+1, to1) + f2(from1*2, to1) + f2(from1**2, to1)
startF1 = time()
print(f1(2, 100)*f1(10,400))
endF1 = time()
startF2 = time()
print(f2(2, 100)*f2(10,400))
endF2 = time()
print(endF1 - startF1, ' F1 time')
print(endF2 - startF2, ' F2 time')  