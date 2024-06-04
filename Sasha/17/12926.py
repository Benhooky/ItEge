f = open('ItEge/Sasha/17/17_12926 (7).txt')
lst = [int(x) for x in f]
Alist = []
List2 = []
List5 = []
max2= -10000000000000
cnt = 0
max4 = -100000000000
for x in range(len(lst)-3):
    cvart = [lst[x],lst[x+1],lst[x+2],lst[x+3]]
    if abs(cvart[0])%10==abs(cvart[1])%10==abs(cvart[2])%10==abs(cvart[3])%10:
        Alist.append(sum(cvart))
A = max(Alist)
for x in lst:
    if 9<abs(x)<100:
        List2.append(x)
max2 = max(List2)
for x in range(len(lst)-4):
    pt5 = [lst[x],lst[x+1],lst[x+2],lst[x+3],lst[x+4]]
    if len([i for i in pt5 if i<A])==1:
        if sum(pt5)%max2==0:
            cnt+=1
            List5.append(sum(pt5))
print(cnt,min(List5))