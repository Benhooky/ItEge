f=open('ItEge/Diana/27/27A_417.txt')
N=f.readline()
lst=[sorted([int(x) for x in l.split()]) for l in f]
summ=0
for i in lst:
    summ+=i[1]
    print(i,i[1]-i[0])
print(summ)