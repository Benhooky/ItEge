f = open('ItEge/Danila/9/9dosrok.txt')
cnt=0
for lst in f:
    lst = sorted(int(x) for x in lst.split())
    first = lst[-1] < sum(lst[:-1])
    second = lst[0] + lst[-1] == lst[1] + lst[2]
    if first and second:
        cnt+=1
print(cnt)