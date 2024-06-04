def troe(x):
    y=""
    while x>0:
        y+=str(x%3)
        x//=3
    return y[::-1]
listansw=[]
for n in range(1,1000):
    i=troe(n)
    if len(i)>1:
        if n%2==0:
            i="2"+i+str(troe(int(i[-1])*2))
        else:
            i=str(troe(int(i[0])*2))+i+"2"
    r=int(i,3)
    if r>100:
        listansw.append(r)
print(min(listansw))