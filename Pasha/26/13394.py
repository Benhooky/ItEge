from math import ceil
f = open('ItEge/Pasha/26/26.6_13394 (1).txt')
n = int(f.readline())
buffer = [int(x) for x in f]
sm_notsale = sum(int(x) for x in buffer if int(x) <= 350)
forSale1 = sorted([int(x) for x in buffer if int(x) > 350])
forSale2 = sorted([int(x) for x in buffer if int(x) > 350])
sumSale = 0
while len(forSale1)>2:
    sumSale+=ceil(forSale1[0]*0.25+forSale1[1]+forSale1[2])
    forSale1 = forSale1[3:]
saleForMarket = 0
while len(forSale2)>2:
    saleForMarket+=forSale2[0]*0.25+forSale2[-1]+forSale2[-2]
    forSale2 = forSale2[1:-2]
print(sumSale+sm_notsale+sum(forSale1), ceil(saleForMarket+sm_notsale+sum(forSale2)))