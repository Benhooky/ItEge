slist=[]
listans=[]
maxSumDigits = 0
lastN = 0
for n in range(1,1000):
    s = "13"*n
    while "13" in s or "31" in s or "11" in s:
        if "13" in s:
            s=s.replace("13","4",1)
        if "31" in s:
            s=s.replace("31","1",1)
        if "11" in s:
            s=s.replace("11","2",1)
        if "44" in s:
            s=s.replace("44","1",1)
    s1 = sum(int(x) for x in s)
    if 10<=s1<=99:
        if s1>maxSumDigits:
            lastN=n
            maxSumDigits=s1
print(lastN)