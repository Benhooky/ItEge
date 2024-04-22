f=open('ItEge/Diana/24/24_4113.txt').readline()
j=0
k=1
maxLen=0

while j!=len(f)-1:
    if len(f)<=k:
        maxLen = max(maxLen,k-2-j+1)
        break
    if f[k-1]==f[k]:
        k+=2
    else:
        maxLen = max(maxLen,k-2-j+1)
        j+=1
        k=j+1
print(maxLen/2)
