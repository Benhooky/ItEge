f=open('ItEge/Ksusha/24/24_11954 (1).txt').readline()
keeperS=''
min1=980798787587
for i in f:
    keeperS+=i
    if keeperS[0]!='X':
        keeperS=''
    if keeperS.count('Y')!=0:
        keeperS=''
    if keeperS.count('X')==500:
        min1=min(min1,len(keeperS))
        keeperS=keeperS[1:]
        keeperS=keeperS[keeperS.index('X'):]
print(min1)

        
