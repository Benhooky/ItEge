def dev(x):
    y=""
    while x>0:
        y+=str(x%9)
        x//=9
    return y[::-1]
for n in range (10000,1,-1):
    i = dev(n)
    a=0
    лист=[]
    for k in range(5):
        if i.count("5") == i.count("7"):
            i = i + i[-1]
        else:
            for x in '012345678':
                лист.append(i.count(x))
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
