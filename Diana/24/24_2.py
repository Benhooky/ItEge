f=open('ItEge/Diana/24/24var04.txt').readline()
lst=[x for x in f.split('E')]
maxLen=0
for x in lst:
    if x.count('A')<=700:
        maxLen=max(maxLen,len(x))
print(maxLen)