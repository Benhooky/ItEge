file=open('Kate/26_7826 (1).txt')
nRoller,nGuests=map(int,file.readline().split())
a=[]
Rollers=[]
for i in range(nRoller):
    Rollers.append([0,0])
for i in range(nGuests):
    tIn,tOut=map(int,file.readline().split())
    a.append([tIn,tOut])
a.sort()
cnt=0
last=0
for i in range(nGuests):
    for j in range(nRoller):
        if (a[i][0]>Rollers[j][1])or(a[i][0]==Rollers[j][0]):
            Rollers[j][0]=a[i][0]
            Rollers[j][1]=max(a[i][1],Rollers[j][1])
            cnt+=1
            last=j+1
print(cnt,last)