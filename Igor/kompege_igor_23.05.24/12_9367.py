for n in range(1,1000):
    s = "1"*40 + "2"*40 + "3"*n
    while "23" in s or "12" in s or "32" in s:
        if "12" in s:
            s=s.replace("12","21",1)
        if "32" in s:
            s=s.replace("32","1",1)
        if "23" in s:
            s=s.replace("23","2",1)
    X=sum([int(x) for x in s])
    if X==100:
        print(n)