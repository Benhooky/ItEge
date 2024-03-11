x=49**7*7**20-7**8-28
def F(n):
    s=''
    while n>0:
        s= str(n%7)+ s
        n//=7
    return s
print(F(x).count("6"))