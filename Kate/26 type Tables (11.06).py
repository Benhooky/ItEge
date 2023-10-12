file=open('Kate/26_8482.txt')
GuestsNum=int(file.readline()[:-1])
TablesNum=int(file.readline()[:-1])
Guests=[]
Tables=[]
for i in range (TablesNum):
    Tables.append([0,0])
for i in range(GuestsNum):
    timeIn,timeOut=map(int,file.readline()[:-1].split())
    Guests.append([timeIn,timeOut+5])
Guests.sort()
cnt=0
last=0
for i in range(GuestsNum):
    Flag=False
    for j in range(TablesNum):
        if Guests[i][0]==Tables[j][0]:
            if Guests[i][1]<Tables[j][1]:
                tmpA=Tables[j][1]
                Tables[j][1]=Guests[i][1]
                last=j+1
                Guests[i]=[Guests[i][0],tmpA]
    for j in range(TablesNum):
        if Guests[i][0]>Tables[j][1]:
            Tables[j][0]=Guests[i][0]
            Tables[j][1]=Guests[i][1]
            cnt+=1
            last=j+1
            Flag=True
            break
    if Flag:continue
    for j in range(TablesNum):
        if Tables[j][1]-Guests[i][0]<10:
            if Guests[i][1]+Tables[j][0]-Guests[i][0]>1380:
                break
            else:
                Tables[j][0]=Tables[j][1]+1
                Tables[j][1]=Guests[i][1]+Tables[j][0]-Guests[i][0]
                cnt+=1
                last=j+1
                break
print(cnt,last)
    