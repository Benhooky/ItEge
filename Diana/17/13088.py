f=open('ItEge/Diana/17/17_13088 (2).txt')
lis =[int(x) for x in f]
max17=0
counter =0
summ=[]
for x in lis:
    if (abs(x))%100==17:
        max17= max(max17,x)


for i in range (len(lis)-2):
    r=lis[i:i+3]
    c=0
    for a in r:
        if len(str(abs(a)))==4:
            c+=1
    if any(x%5==0 for x in r) and c==2:
        if sum(r)>max17:
            counter+=1
            summ.append(sum(r))
print(len(summ),max(summ))
