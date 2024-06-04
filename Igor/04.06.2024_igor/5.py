listansw=[]
for n in range(1,100000):
    i=bin(n)[2:]
    if i.count("1")%2==0:
        i=i+"0"
        i="10"+i[2:]
    else:
        i="1"+i
        i=i[:-2]+"10"
    r=int(i,2)
    if r < 224:
        listansw.append(n)
print(max(listansw))