f=open('Misha/26_7826.txt')
numat , numhum=f.readline().split()
numat=int(numat)
numhum=int(numhum)
attractions=[]
for i in range(numat):
    attractions.append([0,0])
huma=[]
for i in range (numhum):
    tin,tout=f.readline().split()
    tin=int(tin)
    tout=int(tout)
    huma.append([tin,tout])
huma.sort()
cnt=0
lastAt=0
for i in range (len(huma)):
    for q in range(len(attractions)):
        if (attractions[q][1]<huma[i][0])or(attractions[q][0]==huma[i][0]):
            attractions[q][0]=huma[i][0]
            attractions[q][1]=max(attractions[q][1],huma[i][1])
            cnt+=1
            lastAt=q
            break
        
print(cnt,lastAt+1)

