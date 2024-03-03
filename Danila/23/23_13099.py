from functools import lru_cache 
@lru_cache
def f1(from1, to1,flag):
    if from1-1 > to1:
        return 0
    if from1 == to1:
        return 1
    if from1 < to1:
        if flag:
            return f1(from1*2, to1,False) + f1(from1*3, to1,False)
        else:
            return f1(from1-1, to1,True) + f1(from1*2, to1,False) + f1(from1*3, to1,False)
print(f1(3,15,False))