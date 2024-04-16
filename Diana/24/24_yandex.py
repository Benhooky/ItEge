f=open('ItEge/Diana/24/24 (3).txt').readline()
s=0
j=0
k=1
maxLen=0
while s!= len(f)-1:
    current=0
    while f[s]=="C":
        s+=1
    j=s
    k=j+2
    while f[j:k+1]=='ABA' or f[j:k+1]=='BAB':
        current+=1
        j+=3
        k+=3
    maxLen=max(maxLen,current)
    s+=1
print(maxLen)