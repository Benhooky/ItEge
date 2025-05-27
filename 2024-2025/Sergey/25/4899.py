from fnmatch import fnmatch 
cnt=0
def f(x):
    delit=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
for i in range(65000,10000000000000000):
    if fnmatch(str(i),"6*97*5?"):
        delit = f(i)
        cntChet=0
        sumChet=0
        for z in delit:
            if z%2==0:
                cntChet+=1
                sumChet+=z
        if cntChet>=4:
            print(i,sumChet)
            cnt+=1
            if cnt==7:
                break 