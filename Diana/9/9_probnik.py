f = open('ItEge/Diana/9/9.txt')
cnt = 0 
for i in f:
    lst = sorted([int(x) for x in i.split()])
    if (len(set(lst))==len(lst))^((lst[-1]+lst[0])*2<=3*sum(lst[1:-1])):
        cnt+=1
print(cnt)