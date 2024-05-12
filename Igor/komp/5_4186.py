listansw=[]
for n in range(1,1000):
    i=bin(n)[2:]
    if n%2==0:
        i="10"+i
    else:
        i="1"+i+"01"
    r=int(i,2)
    if r>441:
        listansw.append(n)
print(min(listansw))