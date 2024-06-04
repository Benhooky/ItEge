def dev(x):
    y=""
    while x>0:
        y+=str(x%9)
        x//=9
    return y[::-1]
лист=[]
a=0
for n in range (10000,1,-1):
    i = dev(n)
    for k in range(5):
        if i.count("5") == i.count("5"):
            i = i + i[-1]
        else:
            лист.append(i.count("0"))
            лист.append(i.count("1"))
            лист.append(i.count("2"))
            лист.append(i.count("3"))
            лист.append(i.count("4"))
            лист.append(i.count("5"))
            лист.append(i.count("6"))
            лист.append(i.count("7"))
            лист.append(i.count("8"))
            for l in range(9):
                if лист[l]>=a:
                    a=лист[l]
                    dig=l
            i=i+str(dig)
    r=int(i,9)
    r=hex(r)[2:]
    if "bac" in r:
        print(n)
        break
