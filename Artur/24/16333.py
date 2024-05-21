f = open('ItEge/Artur/24/24_16333.txt').readline()
keeperS = ''
maxLen = 0
letters = 'QRW'
digits = '124'
for symbol in f:
    keeperS += symbol
    if len(keeperS)>1:
        if (keeperS[-1] in letters and keeperS[-2] in letters) or (keeperS[-1] in digits and keeperS[-2] in digits):
            maxLen = max(maxLen,len(keeperS)-1)
            keeperS = keeperS[-1]
print(maxLen)