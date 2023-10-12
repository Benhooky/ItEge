a=[int (x) for x in open('Misha/17.txt')]
k=0
s=0
maxa=0
m=0
mins=100000000000000
for x in range (len(a)):
    if abs(a[x])%10==6:
        mins=min(mins,a[x])
for x in range (len(a)-1):
    if (((abs(a[x+1])%10==6)and abs(a[x])%10!=6)  or  ((abs(a[x])%10==6)and (abs(a[x+1])%10!=6)))and(((a[x]**2)+(a[x+1]**2))<(mins**2)):
        m+=1
        maxa=max(maxa,a[x]**2+a[x+1]**2)    
print(m,maxa)
