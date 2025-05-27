def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for i in range(749999,0,-1):
    delit=f(i)
    lst=[]
    for x in delit:
        if len(f(x))==0:
            if x%10==7:
                lst.append(x)
    if len(lst)==0:
        F=0
    else:
        F=sum(lst)//len(lst)
    if F!=0 and F%111==0:
        print(i,F)
        cnt+=1
        if cnt==5:
            break