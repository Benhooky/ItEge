for n in range(4,10000):
    s="4"+n*"0"
    while "40" in s or "800" in s or "000" in s:
        if "40" in s:
            s=s.replace("40","0",1)
        if "800" in s:
            s=s.replace("800","04",1)
        if "000" in s:
            s=s.replace("000","8",1)
    sum1=0 
    for x in s:
        sum1+=int(x)
    if sum1==36:
        print(n)