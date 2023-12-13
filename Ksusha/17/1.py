a=open('ItEge/Ksusha/17/1777.txt')
cnt=0
max29=0
max_sum=0
lis=[int(i) for i in a]
for x in lis:
    if str(x)[-2:]=='29':
        max29=max(max29,x)
for x in range (len(lis)-2):
    cont=0
    for k in range(0, 3):
        if 9999 < abs(lis[x+k]) < 100000:
            cont += 1
    if cont == 2:
        if (lis[x]+lis[x+1]+lis[x+2])<=max29:
            cnt+=1
            max_sum=max(max_sum,(lis[x]+lis[x+1]+lis[x+2]))
print(cnt, max_sum)




