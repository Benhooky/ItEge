for n in range(1,100):
    s=">"+39*"0"+n*"1"+39*"2"
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s=s.replace( ">1", "22>", 1)
        if ">2" in s:
            s=s.replace( ">2", "2>", 1)
        if ">0" in s:
            s=s.replace( ">0", "1>", 1)
    res=0
    for x in s[:-1]:
        res+=int(x)
    isPrime = True
    for x in range(2,res):
        if res%x==0:
            isPrime = False
            break
    if isPrime:
        print(n)
        break
