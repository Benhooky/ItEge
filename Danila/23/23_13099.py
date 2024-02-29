from functools import lru_cache 
@lru_cache
def f1(from1, to1,flag):
    if from1-1 > to1:
        return 0
    if from1 == to1:
        return 1
    if from1 < to1:
        return f1(from1-1, to1,True) if not flag else 0 + f1(from1*2, to1,False) + f1(from1*3, to1,False)
print(f1(3,15,False))