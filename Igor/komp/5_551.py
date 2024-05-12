listansw=[]
for n in range(1,1000):
    i=bin(n)[2:]
    if n%2==0:
        i=i+"01"
    else:
        i=i+"10"
    r=int(i,2)
    if r>73:
        listansw.append(n)
print(min(listansw))