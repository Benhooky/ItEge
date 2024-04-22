f=open('ItEge/Diana/24/24_3900.txt').readline()
'''
f=f.replace('A',' ')
lst=f.split()
print(lst)
res=[]
'''
maxLen=0
keeperS=''
for element in f:
    keeperS+=element
    if keeperS[0]!='A':
        keeperS=''
    if keeperS.count('A')==4:
        keeperS = 'ADBADBADBA'
        str=keeperS.replace('A','*')
        lst = str.split("*")[1:-1]
        if lst[0]==lst[1] and lst[1]==lst[2] and keeperS!='AAAA':
            maxLen=max(maxLen,len(keeperS))
        keeperS=keeperS[1:]
        keeperS=keeperS[keeperS.index('A')-1:]
print(maxLen)
