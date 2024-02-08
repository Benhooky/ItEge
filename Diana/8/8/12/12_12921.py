for n in range (4,10000):
    s= "5"+"2"*n
    while "52" in s or "2222" in s or "1122" in s :
        if "52" in s:
            s=s.replace("52","11",1)
        elif "2222" in s:
            s=s.replace("2222","5",1)
        elif "1122" in s:
            s=s.replace("1122","25",1)
    sumS = sum([int(x) for x in s])
    if sumS%10==7:
        print(n)
        break
