def nechet(x):
    return x%2!=0
def chet(x):
    return x%2==0
def seven(x):
    return x==7
mask = [chet,nechet,chet,chet,nechet,chet,nechet,seven,seven]
for i in range(7777,10**9+1,7777):
    i = str(i)
    if len(i)==9:
        if all(mask[int(j)](int(i[j])) for j in range(9)):
            print(i,int(i)//7777)