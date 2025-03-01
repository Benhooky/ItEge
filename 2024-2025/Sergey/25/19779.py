def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for i in range (55000000,100000000000000):
    mas=f(i)
    minDel=1000000000000
    for x in mas:
        if len(f(x))==0 and x%1000==777:
            minDel=min(minDel,x)
    if minDel!=1000000000000:
        print(i,minDel)
        cnt+=1
        if cnt==4:
            break 
    


