max1 = 0
answerN = 0
for n in range (1,10000):
    i = bin(n)[2:]
    i = int(i)
    i = str(i)
    bit = [x for x in i]
    if i.count("0") > i.count("1"):
        i = i.replace("1","2")
        i = i.replace("0","1")
        i = i.replace("2","0")
    else:
        for index in range(1,len(bit),2):
            bit[index]='1'
        i = "".join(bit)
    r = int(i,2)
    if r <= 1337:
        if r>max1:
            max1 = r
            answerN = n
            print(r,n)
print(answerN)
