f=open('ItEge/Diana/17/17 (16).txt')
lst=[int(x) for x in f]
minA=100000
res=[]
for element in lst:
    if len(str(abs(element)))==4 and element>0:
        if str(abs(element))[-1]==str(abs(element))[-2]:
            minA=min(minA,element)
for i in range(len(lst)-2):
    triple = [lst[i], lst[i+1], lst[i+2]]
    if all(len(str(abs(x)))==3 for x in triple) and sum(triple)>minA:
        res.append(sum(triple))
print(len(res),max(res))