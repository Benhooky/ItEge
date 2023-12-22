f = open("ItEge/Ksusha/17/17_11949.txt")
max_68=0
cnt_4=0
max_4=0
lis=[int(x) for x in f]
for x in lis:
    if abs(x)%100==68:
        max_68=max(max_68,x)
for i in range (len(lis)-3):
    tmp=[lis[i],lis[i+1],lis[i+2],lis[i+3]]
    if all([9<abs(x)<100 for x in tmp]) or [9<abs(x)<100 for x in tmp].count(True)==1:
        if max_68<=sum(tmp):
            cnt_4+=1
            max_4=max(max_4,sum(tmp))
print(cnt_4,max_4)