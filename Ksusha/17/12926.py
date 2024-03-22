g=open('ItEge/Ksusha/17/17_12926 (4).txt')
lst=[int(i) for i in g]
A=-100000000
for x in range (0,len(lst)-3):
    povt=set()
    temp = lst[x:x+4]
    povt = {abs(i) % 10 for i in temp}
    if len(povt)==1:
        A=max(A,sum(temp))

mx2=-10000000000
for e in range(0,len(lst)): 
    if 9<abs(lst[e])<100:
        mx2=max(mx2,lst[e])

Cnt5=0
mn5=999999999999
for i in range (0,len(lst)-4):
    cnt=0
    tmp = lst[i:i+5]
    cnt = [x < A for x in tmp].count(True)
    if cnt==1:
        if sum(tmp)%mx2==0:
            Cnt5+=1
            mn5=min(mn5,sum(tmp))
print(Cnt5,mn5)