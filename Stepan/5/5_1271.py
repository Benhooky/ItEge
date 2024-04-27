def chet(n):
    #sumChet  = sum(1 for x in n if int(x) % 2 == 0)
    sumChet  = len([x for x in n if int(x) % 2 == 0])
    return sumChet
resLst = []
for n in range(1, 1000):
    n8 = oct(n)[2:]
    if chet(n8) % 2 != 0:
        n8 = n8[-3:] + '46'
    else:
        n8 = oct(n % 8 * 5)[2:] + n8
    r = int(n8, 8) 
    if n>=80:
        resLst.append(r)
print(min(resLst))