file=open('Kate/26_8512.txt')
NSel=int(file.readline()[:-1])
NPass=int(file.readline()[:-1])
Pass=[]
Sel=[0]*NSel
for i in range(NPass):
    timeIn,timeOut=map(int,file.readline()[:-1].split())
    Pass.append([timeIn,timeOut])
Pass.sort()
cnt=0
last=0
for i in range(NPass):
    for j in range(NSel):
        if Pass[i][0]>Sel[j]:
            Sel[j]=Pass[i][1]
            cnt+=1
            last=j+1
            break
print(cnt,last)