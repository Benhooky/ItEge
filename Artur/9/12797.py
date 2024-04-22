f = open('ItEge/Artur/9/12797.txt')
count0 = 0
for string in f:
    string = sorted([int(x) for x in string.split()])
    cnt2 = 0
    cnt1 = 0
    flag2 = True
    flag1 = True
    for element in set(string):
        if string.count(element) == 2:
            cnt2 += 1
            if element % 2 != 0:
                flag2 = False
        if string.count(element) == 1:
            cnt1 += 1
            if element % 2 == 0:
                flag1 = False
    if cnt2 == 1 and cnt1 == 2:
        if flag2 and flag1:
            count0 += 1
print(count0)