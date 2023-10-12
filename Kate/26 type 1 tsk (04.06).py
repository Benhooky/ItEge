file=open("Kate/26_7855.txt")
NumRol=int(file.readline()[:-1])
NumGuests=int(file.readline()[:-1])
Time=[]
Rol=[0]*NumRol
for i in range(NumGuests):
    TimeIn,TimeOut=map(int,file.readline().split())
    Time.append([TimeIn,TimeOut+30])
Time.sort()
last=0
timeDelay=0
for i in range(NumGuests):
    flag=False
    for j in range(NumRol-1,0,-1):
        if (Time[i][0]>Rol[j]):
            Rol[j]=Time[i][1]
            last=j+1
            flag=True
            break
    if not flag:
        timeDelay=max(min(Rol)-Time[i][0],timeDelay)
        Rol[Rol.index(min(Rol))]=Time[i][1]
        last=Rol.index(min(Rol))+1
print(timeDelay,last)
