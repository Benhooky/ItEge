def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for i in range(23600000,100000000000):
    mas=[]
    delit=f(i)
    for x in delit:
        if len(f(x))==0:
            mas.append(x)
    if len(mas)==0:
        M=0
    else:
        M=max(mas)+min(mas)
    if M%213==171:
        print(i,M)
        cnt+=1
        if cnt==6:
            break