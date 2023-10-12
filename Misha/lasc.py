from itertools import product
k=0
a=list(product('0123456',repeat=6))
f=''
for x in range(len(a)):
    s=a[x]
    b=0
    for y in range (len(s)):
        if int(s[y])%2==0:b+=1
    if (s[0]!='0') and (int(s[-1])>=4) and( b==3):
        k+=1
        f=s
print(k)
print(f)
