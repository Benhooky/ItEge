f = open('ItEge/2024-2025/Sergey/9/4634.txt')
cnt = 0
for line in f:
    lst = [int(x) for x in line.split()]
    lst.sort()
    if lst[-2]**2>lst[0]*lst[-1]:
        if lst[0]*lst[3]==lst[1]*lst[2]:
            cnt+=1
print(cnt)