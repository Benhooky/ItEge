f = open('ItEge/Ksusha/9/13865.txt')
cnt = 0
for lst in f:
    lst = sorted(int(i) for i in lst.split())
    first = len(set(lst))==len(lst)
    second = 2*(lst[0]+lst[-1])<=sum(lst[1:-1])*3
    usl = [first, second]
    cntUsl = sum(1 for x in usl if x)
    if cntUsl == 1:
        cnt+=1
    #if first ^ second:
        #cnt+=1
print(cnt)