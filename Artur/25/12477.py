from re import fullmatch
def ifProst(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1,10**7+1):
    if fullmatch(r'3\d{1}1111\d{0,}',str(i)):
        if ifProst(i):
            print(i)