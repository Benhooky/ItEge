f = open('ItEge/2024-2025/Sergey/9/demo.txt')
cnt = 0
for line in f:
    lst = [int(x) for x in line.split()]
    lst.sort()
    cnt3 = 0 #количество чисел повторяющихся трижды
    cnt1 = 0 #количество чисел повторяющихся единожды
    sumPovt = 0
    sumN = 0
    for elem in set(lst):
        if lst.count(elem) == 3:
            cnt3 += 1
            sumPovt += elem*3
        if lst.count(elem) == 1:
            cnt1 += 1
            sumN += elem
    if cnt3 == 1 and cnt1 == 3:
        if sumPovt ** 2 > sumN ** 2:
            cnt+=1
print(cnt)