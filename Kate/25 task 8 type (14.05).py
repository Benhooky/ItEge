for N in range(95632,95651):
    a=[]
    for j in range(1,int(N**(1/2))+1):
        if (N%j)==0:
            if j%2!=0 and (j not in a):
                a.append(j)
            if (N//j)%2!=0 and ((N//j) not in a):
                a.append(N//j)
        if len(a)>6:break
    if len(a)==6:
        print(sorted(a))