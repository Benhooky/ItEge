listansw=[]
for n in range(1,1000):
    i = bin(n)[2:]
    summ = (i.count("1"))%2
    i = i + str(summ)
    summ = (i.count("1"))%2
    i = i + str(summ)
    r = int(i,2)
    if r > 452:
        listansw.append(r)
print(min(listansw))

