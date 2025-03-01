def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)

cnt=0
for i in range(902715,100000000000000000):
    mas=f(i)
    minDel=100000000000
    for x in mas:
        if x%10==5 and x!=5:
            minDel=min(minDel,x)
    if minDel!=100000000000:
        print(i,minDel)
        cnt+=1
        if cnt==6:
            break 