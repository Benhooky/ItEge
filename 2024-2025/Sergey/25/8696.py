def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for z in range(1273547,10000000000):
    delit=f(z)
    M=sum(delit)
    if M>0:
        if len(f(M%100000))==0:
            print(z,M)
            cnt+=1
            if cnt==5:
                break