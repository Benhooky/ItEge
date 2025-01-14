f = open("ItEge/2024-2025/Sergey/9/18924.txt")
cnt=0
for line in f:
    lst = [int(x) for x in line.split()]
    lst.sort()
    cnt3=0
    cnt1=0
    sum2Pov=0
    sumNePov=0
    for elem in set(lst):
        if lst.count(elem)== 1:
            cnt1+=1
            sumNePov += elem
        else:
            if lst.count(elem) == 3:
                cnt3 += 1
                sum2Pov+= (elem**2)*3
            else:
                sum2Pov += (elem**2)*lst.count(elem)
    first = cnt3==1 and cnt1==3
    second = sum2Pov > sumNePov**2
    if not(first) and not(second):
        cnt+=1
print(cnt)