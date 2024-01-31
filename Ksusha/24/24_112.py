f=open('ItEge/Ksusha/24/24_11241 (2).txt').readline()[:-1]
keeperS=""
max1=0
lis='ABCD'
for letter in f:
    keeperS+=letter
    if letter in lis:
        max1=max(max1, len(keeperS)-1)
        keeperS=''
print(max1)
    