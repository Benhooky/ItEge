f=open('Misha/24_7272 (1).txt').readline()[:-1]
tr=["AB","CB"]
maxlen=0
for x in tr: f=f.replace(x,"*")
s='*'
while s in f:
    s+='*'
print(len(s)-1)