f=open("ItEge/Ksusha/24/241111111111.txt").readline()
kepS=''
cnt=0
ans=[]
for letter in f:
    kepS+=letter
    if kepS.count('.')==6:
        ans.append(len(kepS)-1)
        kepS = kepS[kepS.index('.')+1:]
print(max(ans))