from  fnmatch import fnmatch
for x in range (0,10**6):
    cntDel = 0
    maxDel = 0
    for i in range(1,int(x**0.5)):
        if x%i==0:
            if fnmatch(str(i),'4*'):
                cntDel+=1
                maxDel=max(maxDel,i)
            if fnmatch(str(x//i),'4*'):
                cntDel+=1
                maxDel=max(maxDel,x//i)
        if cntDel > 24:
            break
    if cntDel==24:
        print(x,maxDel)