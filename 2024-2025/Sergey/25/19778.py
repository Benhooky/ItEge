def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
cnt=0
for i in range(9500001,1000000000000000000):
    mas=f(i) # делители нашего числа
    F = 0
    cntDel = 0
    for x in mas:
        if len(f(x))==0: # если делитель - число простое
            F+=x
            cntDel+=1
    F=F//cntDel if cntDel>0 else 0
    if F!=0 and F%813==0:
        print(i, F)
        cnt+=1
        if cnt==5:
            break