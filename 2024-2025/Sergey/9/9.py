f = open('ItEge/2024-2025/Sergey/9/7030.txt')
number = 0
answer = 0
for line in f:
    number+=1
    lst = [int(x) for x in line.split()]
    lst.sort()
    cnt2 = 0
    cnt1 = 0
    for elem in set(lst):
        if lst.count(elem) == 2:
            cnt2 += 1
        elif lst.count(elem) == 1:
            cnt1 += 1
    first = cnt2 == 3 and cnt1 == 0
    second = lst[-1]**2 == lst[0]**2 + lst[2] ** 2
    if first and second:
        answer = number
print(answer)