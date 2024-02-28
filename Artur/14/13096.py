n = 17
k = 0
result = 0
a = 8
while n > 0:
    result+=n%10*a**k
    k+=1
    n//=10
print(result)