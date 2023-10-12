f=open('')
k= int(f.readline())
n= int(f.readline())
a=[]
people=[0]*n
attraction=[0]*k
for i in range (n):
    Time=f.readline()
    x,y=Time.split()
    human.append([int(x),int(y)])
human.sort()
for i in range (n):
    if human[i-1][0] and people[i-1]>0:
        attraction[people[i-1]-1]= int(y)
        people[i]=people[i-1]
        continue
    for nu in range (k):
        if x>attractions[nu]:
            attractions[nu]=y
            people[i]= nu+1
            break
print(sum(1 for numb in people if nu>0))
