listansw=[]
for n in range(1,1000):
    i=bin(n)[2:]
    for cicle in range(2):
        if i.count("1")%2==0:
            i=i+"0"
        else:
            i=i+"1"
    r=int(i,2)
    if r > 121:
        listansw.append(n)
print(min(listansw))