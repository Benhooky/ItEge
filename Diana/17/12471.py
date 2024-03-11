f = open('ItEge/Diana/17/17_12471 (1).txt')
lis = [int(x) for x in f]
max13 = 0
c=0
summ=0
max13 = max(x for x in lis if abs(x)%100==13)#1
for i in lis:#2
    if abs(i)%100 == 13:
        max13=max(max13,i)
for i in range(len(lis)-2):
    r = lis[i:i+3]
    if all(x%2==0 for x in r) or any(len(str(abs(x)))==2 for x in r):
        if sum(r)<=max13:
            c+=1
            summ+=sum(r)
print(c,summ//c)