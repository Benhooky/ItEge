def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)

cnt=0
for i in range(1200001,1000000000000000):
    mas=f(i)
    minDel=1000000000000
    maxDel=0
    for x in mas:
        if len(f(x))==0:
            minDel=min(minDel,x)
            maxDel=max(maxDel,x)
    M=maxDel+minDel
    if M>2000 and M%10==8:
        print(i,M)
        cnt+=1
        if cnt==5:
            break