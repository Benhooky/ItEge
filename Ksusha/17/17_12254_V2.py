f=open("ItEge/Ksusha/17/17_12249.txt")
max_5=0
cnt3=0
max_3=0
lis=[int(i) for i in f]
for i in lis:
    if (9999<i<100000) and abs(i)%10==5:
        max_5=max(max_5,i)
for i in range(len(lis)-2):
    tmp=[lis[i],lis[i+1],lis[i+2]]
    if any([abs(x)%10==3 for x in tmp]):
        if sum(tmp)<=max_5:
            cnt3+=1
            max_3=max(max_3, sum(tmp))
print(cnt3,max_3)
