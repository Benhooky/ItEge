f=open('ItEge/Diana/27/27-A_1067.txt')
N=int(f.readline())
lst=[[int(y[0]),int(y[1]),abs(int(y[1])-int(y[0]))] for y in [x.split() for x in f]]
print(lst)
res1=[]
res2=[]
cnt1=0
cnt2=0
ind=[]
for i in range(N):
    if lst[i][1]%2==0:
        res1.append(lst[i][1])
        cnt1+=1
    elif lst[i][1]%2!=0:
        res1.append(lst[i][1])
    if lst[i][0]%2==0:
        res2.append(lst[i][0])
        cnt2+=1
    elif lst[i][0]%2!=0:
        res2.append(lst[i][0])

    print(res1)
    print(res2)
    print(cnt1,cnt2)
#надо поменять 21 и 20 местами, тогда выполнится условие задачи
#очень маленький файл
#print(27+26+30+21+22+23+15+29+27+18+20+22+23+14+24+27+23+27+20+13)