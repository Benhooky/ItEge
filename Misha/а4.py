f=open('Misha/27_B_7275 (1).txt')
n, m= map(int, f.readline().split())
a=[]
maxS=0
for x in range (n):
    nu, co=map(int, f.readline().split())
    if  co%30>0: co=(co//30)+1
    else: co=co//30
    a.append([nu,co])
for x in range (len(a)):
    sOfCont=0
    for y in range (x-m,x+m+1):
            if 0<=y<=n-1:
                 if a[x][0]-m<=a[y][0]<=a[x][0]+m:
                      sOfCont+=a[y][1]
    maxS=max(maxS,sOfCont)
print(maxS)