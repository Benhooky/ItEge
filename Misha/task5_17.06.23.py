import sys
sys.setrecursionlimit(1500)
def H(x):
    if x>=4040:
        return x
    if x<4040:
        return x+4+H(x+4)
print(H(3)-H(15))