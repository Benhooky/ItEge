from math import ceil
f=open('ItEge/Ksusha/26/26.6_13394.txt')
N=int(f.readline())
buffer = [int(i) for i in f]
sumWithoutSale = sum(int(i) for i in buffer if int(i)<=350)
lst1=sorted(int(i) for i in buffer if int(i)>350)
lst2=sorted(int(i) for i in buffer if int(i)>350)
sumSale=0
sumAll=0
while len(lst1)>2:
    sumSale+=ceil((lst1[0]*0.25)+lst1[1]+lst1[2])
    lst1=lst1[3:]
while len(lst2)>2:
    sumAll+=((lst2[0]*0.25)+lst2[-1]+lst2[-2])
    lst2=lst2[1:-2]
print(sumSale+sumWithoutSale+sum(lst1),ceil(sumAll+sumWithoutSale+sum(lst2)))