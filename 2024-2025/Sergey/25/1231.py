def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for z in range(250200,100000000):
    delit=f(z)
    if len(delit)>0:
        if (max(delit)+min(delit))%123==17:
            print(z,max(delit)+min(delit))
            cnt+=1
            if cnt==5:
                break 