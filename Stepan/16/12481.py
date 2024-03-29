import sys
sys.setrecursionlimit(10000)
def F(n):
    if n<5:
        return 4
    else:
        return 4*F(n-4)
print(F(4444)/F(4400))