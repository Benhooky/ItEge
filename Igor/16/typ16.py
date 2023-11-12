import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n < 10:
        return n
    if n >=10:
        return n%10 + 8*F(n//10) 
print(F(10**30))