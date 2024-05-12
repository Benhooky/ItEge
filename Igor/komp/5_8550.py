listansw=[]
for n in range(1,10000):
    i=bin(n)[2:]
    if n%3==0:
        i = "10" + i[2:] + "1"
    else:
        i = bin((n%3)*2)[2:] + i
    r=int(i,2)
    if r>8000:
        listansw.append(r)
print(min(listansw))